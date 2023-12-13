import json
import numpy as np
import os

annots = json.load(open('annots.json', 'r'))

new_annots = {}
new_annots['cams'] = annots['cams']['20190823']
ims = annots['ims']
for im in ims:
    img_paths = im['ims']
    img_paths = [os.path.join(*i.split('/')[1:]) for i in img_paths]
    im['ims'] = img_paths
    del im['cams_set']
    del im['kpts3d']

new_annots['ims'] = ims[:1470]
np.save('annots.npy', new_annots)
np.save('annots_python2.npy', new_annots, fix_imports=True)
