pyprogressbar
=============

###1. Introduction

pyprogressbar is a progress bar control for python.

#####Please feel free to contact me [tanggefu@gmail.com] if you have any questions.

###2. Install

This package uses distutils, which is the default way of installing python modules. To install in your home directory, securely run the following:
```
git clone https://github.com/primetang/pyprogressbar.git
cd pyprogressbar
python setup.py install
```

Or directly through `pip` to install it:
```
pip install pyprogressbar
```

###3. Usage

Use it just like the following code:
```python
from pyprogressbar import Bar
import time
count = 8
pbar = Bar(count)
for i in xrange(count):
    time.sleep(1) # or some actual working code
    pbar.passed()
```

And the effect of the progress bar is:
```
0%   10   20   30   40   50   60   70   80   90   100%
|----|----|----|----|----|----|----|----|----|----|
******************
```
