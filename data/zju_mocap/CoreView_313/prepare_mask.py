import cv2
import os
import numpy as np
import imageio
from tqdm import tqdm
import glob


class CV_KEY:
    BLANK = 32
    ENTER = 13
    LSHIFT = 225  # Mac上不行
    NONE = 255
    TAB = 9
    q = 113
    ESC = 27
    BACKSPACE = 8
    WINDOW_WIDTH = int(1920 * 0.9)
    WINDOW_HEIGHT = int(1080 * 0.9)
    LEFT = ord('a')
    RIGHT = ord('d')
    UP = ord('w')
    DOWN = ord('s')


def get_key():
    k = cv2.waitKey(10) & 0xFF
    if k == CV_KEY.LSHIFT:
        key1 = cv2.waitKey(500) & 0xFF
        if key1 == CV_KEY.NONE:
            return key1
        k = key1 - ord('a') + ord('A')
    return k


def switch_frame(k, nf, total_frames):
    if k == ord('d') or k == CV_KEY.BLANK:
        cur_nf = min(total_frames - 1, nf + 1)
    elif k == ord('a'):
        cur_nf = max(0, nf - 1)
    else:
        cur_nf = nf
    return cur_nf


# mouse callback function
drawing = False
ix, iy = -1, -1
clean = 0
size = 3


def draw_circle(event, x, y, flags, param):
    global ix, iy, drawing, mode

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.circle(param['msk'], (x, y), size, (1 - clean, ), -1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.circle(param['msk'], (x, y), size, (1 - clean, ), -1)


def adjust_hsv(img):
    saturation = 3
    brightness = 3
    contrast = 3

    hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
    hsv = hsv.astype(np.float32)
    hsv[..., 1] = hsv[..., 1] * saturation
    hsv[..., 1] = np.minimum(hsv[..., 1], 255)
    hsv[..., 2] = hsv[..., 2] * brightness
    hsv[..., 2] = np.minimum(hsv[..., 2], 255)
    hsv = hsv.astype(np.uint8)
    img = cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB)
    img = img.astype(np.float32) * contrast
    img = np.minimum(img, 255)
    img = img.astype(np.uint8)

    return img


def read_img(img_path):
    img = cv2.imread(img_path)
    img = adjust_hsv(img)
    cv2.putText(img, '{}'.format(img_path), (10, 50), cv2.FONT_HERSHEY_SIMPLEX,
                1, (0, 0, 255), 2)
    return img


def read_mask(msk_path, cache_msk_path):
    if os.path.exists(cache_msk_path):
        msk = imageio.imread(cache_msk_path)
    else:
        msk = imageio.imread(msk_path)
    return msk


def draw_key_frame(img, img_path, frames):
    if img_path not in frames:
        return
    cv2.rectangle(img, (0, 0), (img.shape[1], img.shape[0]), (0, 0, 255),
                  img.shape[1] // 100)


msk_dirs = ["mask_cihp/Camera ({})".format(i) for i in [1, 7, 13, 19]]
msk_paths = [glob.glob(os.path.join(msk_dir, '*')) for msk_dir in msk_dirs]
msk_paths = [sorted(msk_path) for msk_path in msk_paths]

num_of_frames = 60
msk_paths = [msk_path[:num_of_frames] for msk_path in msk_paths]
msk_paths = np.array(msk_paths).ravel()
img_paths = [os.path.join(*msk_path.split('/')[1:]) for msk_path in msk_paths]
img_paths = [i.replace('.png', '.jpg') for i in img_paths]
cache_msk_paths = [
    os.path.join('cache_masks',
                 *m.split('/')[1:]) for m in msk_paths
]

cur_nf = 0
total_frames = len(img_paths)
img = read_img(img_paths[cur_nf])
msk = read_mask(msk_paths[cur_nf], cache_msk_paths[cur_nf])
msk_ = np.ones_like(img) * 255
msk_[msk == 0] = 0
ratio = 0.5
blend = (img * ratio + msk_ * (1 - ratio)).astype(np.uint8)
param = {'img': img, 'msk': msk, 'img_path': img_paths[cur_nf]}

base = 'main'
cv2.namedWindow(base)
cv2.setMouseCallback(base, draw_circle, param)
sizes = [ord('{}'.format(i)) for i in range(1, 10)]

pbar = tqdm(total=total_frames)

while True:
    msk_ = np.ones_like(img) * 255
    msk_[msk == 0] = 0
    blend = (img * ratio + msk_ * (1 - ratio)).astype(np.uint8)
    cv2.imshow(base, blend)
    k = get_key()
    if k in [ord('d'), ord('a')]:
        os.system("mkdir -p '{}'".format(os.path.dirname(
            cache_msk_paths[cur_nf])))
        cv2.imwrite(cache_msk_paths[cur_nf], param['msk'])
        cur_nf = switch_frame(k, cur_nf, total_frames)
        img = read_img(img_paths[cur_nf])
        msk = read_mask(msk_paths[cur_nf], cache_msk_paths[cur_nf])
        param['msk'] = msk
        pbar.n = cur_nf
        pbar.last_print_n = max(cur_nf - 1, 0)
        pbar.update(0)
    elif k == ord('v'):
        clean = 1 - clean
    elif k in sizes:
        size = int(k - ord('0'))
    if k == CV_KEY.ESC:
        break
pbar.close()
