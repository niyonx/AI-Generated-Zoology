'''
shuffles all files in INPUT_PATH folder into TRAIN_PATH and TEST_PATH according to given ratios
note that train and test folders should be empty or non-existent. If you want script to delete files from them for you, set CLEAR_DIR to True
'''

import numpy as np
import os
import random
import shutil

CLEAR_DIR = False
INPUT_PATH = 'data/resized_combined/'
TRAIN_PATH = 'data/train/'
TEST_PATH = 'data/test/'
TEST_RATIO = 0.05

assert os.path.isdir(INPUT_PATH), INPUT_PATH + ' does not exist'
assert TEST_RATIO >=0 and TEST_RATIO<=1, "TEST_RATIO must be between 0 and 1"
for dir_path in [TRAIN_PATH, TEST_PATH]:
    if os.path.isdir(dir_path):
        if CLEAR_DIR and len(os.listdir(dir_path)) != 0:
            for filename in os.listdir(dir_path):
                os.remove(dir_path+filename)
        else:
            assert len(os.listdir(dir_path)) == 0, dir_path + " is not empty, clear it first or set CLEAR_DIR to True"
    else:
        os.mkdir(dir_path)


input_dir = os.listdir(INPUT_PATH)
random.shuffle(input_dir)

for i,filename in enumerate(input_dir):
    if i <= TEST_RATIO * len(input_dir):
        shutil.copy(INPUT_PATH+filename, TEST_PATH+filename)
    else:
        shutil.copy(INPUT_PATH+filename, TRAIN_PATH+filename)

