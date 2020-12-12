'''
converts .png files to .jpeg from PATH dir
This is needed for now, since PhotoSketch doesn't seem to work on .png files even though it should.
'''

from PIL import Image
import os


PATH = "data/raw-img/"
assert os.path.isdir(PATH), PATH + " dir doesn't exist"

for filename in os.listdir(PATH):
    if filename.split('.')[1] != 'jpeg':
        print('converting file: {}'.format(filename))
        img = Image.open(PATH + filename)
        img = img.convert('RGB')
        img.save('{}{}{}'.format(PATH, filename.split('.')[0], '.jpeg'))
        os.remove(PATH + filename)