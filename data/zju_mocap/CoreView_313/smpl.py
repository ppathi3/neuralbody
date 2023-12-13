import os
import json
import numpy as np
import cv2
import sys
sys.path.append('/mnt/data/home/pengsida/Codes/SMPL_CPP/build/python')
import pysmplceres
import open3d as o3d
import pyskeleton

# initialize a smpl model
pysmplceres.loadSMPL('/mnt/data/home/pengsida/Codes/SMPL_CPP/model/smpl/',
                     'smpl')

param_path = '/home/pengsida/Datasets/light_stage/params/CoreView_313/100.npy'
params = np.load(param_path, allow_pickle=True).item()
params['poses'][:] = 0
params['Rh'][:] = 0
params['Th'][:] = 0
vertices = pysmplceres.getVertices(params)[0]
np.save('v_shaped.npy', vertices)
