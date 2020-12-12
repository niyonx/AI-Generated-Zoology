# AI-Generated-Zoology

Our goal is to be able to convert an animal sketch to an animal picture.

## Set-up project

1. Git clone the repository

```
git clone https://github.com/niyonx/AI-Generated-Zoology.git
```

2. Create your python virtual environment

```
virtualenv --python=/usr/bin/python3.8 venv
source venv/bin/activate
```

3. Install dependencies

```
pip install -r requirements.txt
```

## Run Jupyter Notebooks:

**Locally**: Make sure jupyter is using venv python interpreter.

```
jupyter lab
```


## Images to sketch
If you start from scratch, then you only have images with background removed by some means. We used photoshop.
1. Place all your images in 
```
data/raw-img/
```
2. Edge detection model only works on jpeg files, so convert all images by running
```
./scripts/png_to_jpeg.py
```
3. From PhotoSketch directory, run
```
./scripts/test_pretrained.sh (Linux)
```
```
./scripts/test_pretrained.cmd (Windows, can run from any directory or just double click on file)
```
4. Sketch images should be located in:
```
./data/sketh-img/
```


## Project data
For demo purposes, we placed only a small portion of the datasets we used.\
The full data we used for the project can be downloaded from: https://drive.google.com/file/d/1pzdkQ1OBVexu6YrW_ULHg_lUDiOu2ef1/view?usp=sharing


## Checkpoints
We saved our models after 500 epochs for both cats and dogs datasets.\
However, due to their large size, we make them available at: https://drive.google.com/file/d/1TH6DImrtBW70vWCeLD5ro7tA_LRlv4qG/view?usp=sharing


## Demo
Simply run all the cells up to the RESULTS section.<br>
DO NOT run the cells below RESULTS.<br>
We ran those cells with the checkpoints loaded to showcase our results.<br>
You would need to download the checkpoints to run those cells.<br>
<br>
We have added some of our results in *data/results(dogs)* and *data/results(cats)*