'''
resizes all images from RAW_PATH and SKETCH_PATH to 256x256, stacks them horizontally and saves to a new folder 'combined'
assumes files in raw-img and sketch-img are named the same and all raw-img files have a coresponding sketch-img
'''

import numpy as np
from PIL import Image
import os

def get_concat_h(im1, im2):
    dst = Image.new('RGB', (im1.width + im2.width, im1.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width, 0))
    return dst


RAW_PATH = 'data/raw-img/'
SKETCH_PATH = 'data/sketch-img/'
IMG_SIZE = (256,256)
RESULT_PATH = 'data/combined/'
if not os.path.exists(RESULT_PATH):
    os.mkdir(RESULT_PATH)

raw_dir = os.listdir(RAW_PATH)
sketch_dir = os.listdir(SKETCH_PATH)
combined_dir = zip(raw_dir, sketch_dir)

for raw_file, sketch_file in combined_dir:
    raw_img = Image.open('{}{}'.format(RAW_PATH, raw_file))
    raw_img = raw_img.resize(IMG_SIZE)
    sketch_img = Image.open('{}{}'.format(SKETCH_PATH, sketch_file))
    sketch_img = sketch_img.resize(IMG_SIZE)
    
    merged_img = get_concat_h(raw_img, sketch_img)
    merged_img.save('{}{}'.format(RESULT_PATH, raw_file))


