**(Semi) Automated Image Processing**

[![DOI](https://zenodo.org/badge/249137364.svg)](https://zenodo.org/badge/latestdoi/249137364)
![Test-Package](https://github.com/Nelson-Gon/pyautocv/workflows/Test-Package/badge.svg)
![Travis Build](https://travis-ci.com/Nelson-Gon/pyautocv.svg?branch=master)
[![PyPI version fury.io](https://badge.fury.io/py/pyautocv.svg)](https://pypi.python.org/pypi/pyautocv/)
[![PyPI license](https://img.shields.io/pypi/l/pyautocv.svg)](https://pypi.python.org/pypi/pyautocv/)
[![PyPI download Month](https://img.shields.io/pypi/dm/pyautocv.svg)](https://pypi.python.org/pypi/pyautocv/)
[![PyPI download week](https://img.shields.io/pypi/dw/pyautocv.svg)](https://pypi.python.org/pypi/pyautocv/)
[![PyPI download day](https://img.shields.io/pypi/dd/pyautocv.svg)](https://pypi.python.org/pypi/pyautocv/)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Nelson-Gon/pyautocv/graphs/commit-activity)
[![Project Status](http://www.repostatus.org/badges/latest/active.svg)](http://www.repostatus.org/#active) 
[![GitHub last commit](https://img.shields.io/github/last-commit/Nelson-Gon/pyautocv.svg)](https://github.com/Nelson-Gon/pyautocv/commits/master)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![GitHub issues](https://img.shields.io/github/issues/Nelson-Gon/pyautocv.svg)](https://GitHub.com/Nelson-Gon/pyautocv/issues/)
[![GitHub issues-closed](https://img.shields.io/github/issues-closed/Nelson-Gon/pyautocv.svg)](https://GitHub.com/Nelson-Gon/pyautocv/issues?q=is%3Aissue+is%3Aclosed)
[![license](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/Nelson-Gon/pyautocv/blob/master/LICENSE)

**Project Aims**

The goal of simple cv is to provide a simple computer vision(cv) workflow that enables one to automate 
or at least reduce the time spent in image (pre)-processing. 

**Installing the package**

From pypi:

```

pip install pyautocv

```
From GitHub

```
# only if you can see releases >= 1
pip install pip install git+https://github.com/Nelson-Gon/pyautocv.git
# clone the repo
git clone https://www.github.com/Nelson-Gon/pyautocv.git
cd pyautocv
python3 setup.py install

```



**Example Usage**

```
from pyautocv.segmentation import *
images_list=Segmentation("images")
images_list.show_images(thresholded=False,ncols=2)

```

The above will give us the following result:


![Sample_colored](./sample_results/sample_colored.png)