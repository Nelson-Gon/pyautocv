**(Semi) Automated Image Processing**

![Stage](https://www.repostatus.org/badges/latest/wip.svg) [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3766956.svg)](https://doi.org/10.5281/zenodo.3766956)
![Test-Package](https://github.com/Nelson-Gon/pyautocv/workflows/Test-Package/badge.svg)
![Travis Build](https://travis-ci.com/Nelson-Gon/pyautocv.svg?branch=master)
[![PyPI version fury.io](https://badge.fury.io/py/pyautocv.svg)](https://pypi.python.org/pypi/pyautocv/)
[![PyPI license](https://img.shields.io/pypi/l/pyautocv.svg)](https://pypi.python.org/pypi/pyautocv/)
[![PyPI download Month](https://img.shields.io/pypi/dm/pyautocv.svg)](https://pypi.python.org/pypi/pyautocv/)
[![PyPI download week](https://img.shields.io/pypi/dw/pyautocv.svg)](https://pypi.python.org/pypi/pyautocv/)
[![PyPI download day](https://img.shields.io/pypi/dd/pyautocv.svg)](https://pypi.python.org/pypi/pyautocv/)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Nelson-Gon/pyautocv/graphs/commit-activity)
[![GitHub last commit](https://img.shields.io/github/last-commit/Nelson-Gon/pyautocv.svg)](https://github.com/Nelson-Gon/pyautocv/commits/master)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![GitHub issues](https://img.shields.io/github/issues/Nelson-Gon/pyautocv.svg)](https://GitHub.com/Nelson-Gon/pyautocv/issues/)
[![GitHub issues-closed](https://img.shields.io/github/issues-closed/Nelson-Gon/pyautocv.svg)](https://GitHub.com/Nelson-Gon/pyautocv/issues?q=is%3Aissue+is%3Aclosed)
[![license](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/Nelson-Gon/pyautocv/blob/master/LICENSE)

**Project Aims**

The goal of pyautocv is to provide a simple computer vision(cv) workflow that enables one to automate 
or at least reduce the time spent in image (pre)-processing. 

**Installing the package**

From pypi:

```

pip install pyautocv

```
From GitHub

```
pip install pip install git+https://github.com/Nelson-Gon/pyautocv.git
#or
# clone the repo
git clone https://www.github.com/Nelson-Gon/pyautocv.git
cd pyautocv
python3 setup.py install

```

**Available Class**

* Segmentation is a super class on which other classes build

* EdgeDetection is dedicated to edge detection. Currently supported kernels are stored in `.available_operators()`

* Thresholding dedicated to thresholding.



**Example Usage**

* Smoothing

To smooth a directory of images, we can use `EdgeDetection`'s `smooth` method as
follows:

```python

to_smooth = EdgeDetection("images/people","sobel_vertical","box")
show_images(*[to_smooth.gray_images(), to_smooth.smooth()])

```

This will give us;

![Smoothened](sample_results/smooth_images.png)


* Edge Detection 

To detect edges in a directory image, we provide original(grayed) images for comparison to
images that have been transformed to detect edges. 

```
from pyautocv.segmentation import *
edge_detection = EdgeDetection("images","sobel_vertical","box")

show_images(*[edge_detection.gray_images(), edge_detection.detect_edges()])

```

The above will give us the following result:


![Sample_colored](./sample_results/images_smooth.png)

To use a different filter e.g Laplace,

```
show_images(*[edge_detection.gray_images(), edge_detection.detect_edges(operator="laplace")])

```

This results in:

![Laplace](./sample_results/show_smooth_laplace.png)


* Thresholding

To perform thresholding, we can use `Threshold`'s methods dedicated to thresholding.

We use flowers as an example:

```
to_threshold = Threshold("images/flowers",threshold_method="simple")
show_images(to_threshold.gray_images(),to_threshold.threshold_images())

```

![Flowers](./sample_results/threshold_flowers.png)



These and more examples are available in [example2.py](./examples/example2.py). Image sources are
shown in `sources.md`. If you feel, attribution was not made, please file an issue
and cite the violating image.

> Thank you very much

> “A language that doesn't affect the way you think about programming is not worth knowing.”
― Alan J. Perlis


---

References:

* [Bebis](https://www.cse.unr.edu/~bebis/CS791E/Notes/EdgeDetection.pdf)
