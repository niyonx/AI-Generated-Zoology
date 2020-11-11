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

**Online**: Upload notebook on [Google Colab](https://colab.research.google.com/notebooks/intro.ipynb#recent=true).


## Images to sketch

1. Input is in data/raw-img

2. From PhotoSketch directory run

```
./scripts/test_pretrained.sh (Linux)
```
3. Output sketches will be in data/sketch-img

If on windows, run test_pretrained.cmd file. Input and Output directory can be modified from scripts/test_pretrained file. [More info](https://github.com/mtli/PhotoSketch).