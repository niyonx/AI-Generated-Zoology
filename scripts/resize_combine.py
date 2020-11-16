'''
resizes all images from RAW_PATH and SKETCH_PATH to 256x256, stacks them horizontally and saves to a new folder RESULT_PATH
'''

import numpy as np
from PIL import Image
import os

#stacks two images horizontally
def get_concat_h(im1, im2):
    dst = Image.new('RGB', (im1.width + im2.width, im1.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width, 0))
    return dst


RAW_PATH = 'data/raw-img/'
SKETCH_PATH = 'data/sketch-img/'
IMG_SIZE = (256,256)
RESULT_PATH = 'data/resized_combined/'

#make sure that RESULT_PATH is an empty dir
if os.path.isdir(RESULT_PATH):
    assert len(os.listdir(RESULT_PATH)) == 0, RESULT_PATH + " is not empty, clear it first"
else:
    os.mkdir(RESULT_PATH)


raw_dir = os.listdir(RAW_PATH)
sketch_dir = os.listdir(SKETCH_PATH)
assert len(raw_dir) == len(sketch_dir), '{} and {} have different number of files'.format(RAW_PATH, SKETCH_PATH)
result_dir = zip(raw_dir, sketch_dir)


for raw_file, sketch_file in result_dir:
    assert raw_file.split('.')[0] == sketch_file.split('.')[0], 'raw_file: ' + raw_file + "  and sketch_file: " + sketch_file\
        +"  don't have matching names. Maybe clear " + SKETCH_PATH + " and run PhotoSketch model again"
    raw_img = Image.open('{}{}'.format(RAW_PATH, raw_file))
    raw_img = raw_img.resize(IMG_SIZE)
    sketch_img = Image.open('{}{}'.format(SKETCH_PATH, sketch_file))
    sketch_img = sketch_img.resize(IMG_SIZE)
    
    merged_img = get_concat_h(raw_img, sketch_img)
    merged_img.save('{}{}{}'.format(RESULT_PATH, raw_file.split('.')[0], '.jpeg'))

