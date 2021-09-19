# (Semi) Automated Image Processing with pyautocv

[![PyPI version fury.io](https://badge.fury.io/py/pyautocv.svg)](https://pypi.python.org/pypi/pyautocv/)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3766956.svg)](https://doi.org/10.5281/zenodo.3766956)
![Stage](https://www.repostatus.org/badges/latest/active.svg) 
![Actions](https://github.com/Nelson-Gon/pyautocv/workflows/Test-Package/badge.svg)
[![Codecov](https://codecov.io/gh/Nelson-Gon/pyautocv/branch/master/graph/badge.svg)](https://codecov.io/gh/Nelson-Gon/pyautocv?branch=master)
[![license](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/Nelson-Gon/pyautocv/blob/master/LICENSE)
[![Documentation Status](https://readthedocs.org/projects/pyautocv/badge/?version=latest)](https://pyautocv.readthedocs.io/en/latest/?badge=latest)
[![PyPI license](https://img.shields.io/pypi/l/pyautocv.svg)](https://pypi.python.org/pypi/pyautocv/)
[![Total Downloads](https://pepy.tech/badge/pyautocv)](https://pepy.tech/project/pyautocv)
[![Monthly Downloads](https://pepy.tech/badge/pyautocv/month)](https://pepy.tech/project/pyautocv)
[![Weekly Downloads](https://pepy.tech/badge/pyautocv/week)](https://pepy.tech/project/pyautocv)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Nelson-Gon/pyautocv/graphs/commit-activity)
[![GitHub last commit](https://img.shields.io/github/last-commit/Nelson-Gon/pyautocv.svg)](https://github.com/Nelson-Gon/pyautocv/commits/master)
[![GitHub issues](https://img.shields.io/github/issues/Nelson-Gon/pyautocv.svg)](https://GitHub.com/Nelson-Gon/pyautocv/issues/)
[![GitHub issues-closed](https://img.shields.io/github/issues-closed/Nelson-Gon/pyautocv.svg)](https://GitHub.com/Nelson-Gon/pyautocv/issues?q=is%3Aissue+is%3Aclosed)


**Project Aims**

The goal of `pyautocv` is to provide a simple computer vision(cv) workflow that enables one to automate 
or at least reduce the time spent in image (pre)-processing. 

**Installing the package**

From PyPI

```shell

pip install pyautocv

```
From GitHub

```shell
pip install git+https://github.com/Nelson-Gon/pyautocv.git
#or
# clone the repo
git clone https://www.github.com/Nelson-Gon/pyautocv.git
cd pyautocv
python3 setup.py install

```



**Example Usage**

**Note**: Although these methods can be run via this script, the script is less flexible and might be useful for quick
exploration but not extended analysis. 


To run the script at the  commandline, we can do the following

```shell

python -m pyautocv -d "images/cats" -s "png" -m "thresh_to_zero" -o "threshold" -mt 200 -t 100

```

Sample Result

![Command Line Script](https://github.com/Nelson-Gon/pyautocv/blob/master/sample_results/sample_script.png?raw=true)


To perform edge detection

```shell

python -m pyautocv -d "images/biology" -s "jpg" -o "detect_edges" -m "sobel_vertical" -k 3
```

![Bio Script](https://github.com/Nelson-Gon/pyautocv/blob/master/sample_results/bioscript.png?raw=true)


To smooth images

```shell
python -m pyautocv -d "images/houses" -s "jpg" -o "smooth" -m "gaussian" -k 5 5 --sigma 0.7
```

![Houses Smooth](https://github.com/Nelson-Gon/pyautocv/blob/master/sample_results/houses_smooth.png?raw=true)

To get help

```shell

python -m pyautocv -h 



```

Further exploration is left to the user.

---

The following section shows how to use the more flexible class/methods approach

* Image Gra(e)ying

To grey an image directory

```python
from pyautocv.segmentation import Segmentation, gray_images, show_images

images_list=Segmentation("images/cats")
show_images(gray_images(images_list.read_images()), images_list.read_images(), number=2)

```
![Grayed](https://github.com/Nelson-Gon/pyautocv/blob/master/sample_results/cats_gray.png?raw=true)

* Smoothing

To smooth a directory of images, we can use `EdgeDetection`'s `smooth` method as
follows

```python

images_list=Segmentation("images/cats")
show_images(images_list.smooth(), images_list.read_images(),number=2)

```

This will give us

![Smooth](https://github.com/Nelson-Gon/pyautocv/blob/master/sample_results/cats_smooth.png?raw=true)

The above uses default parameters including an `rgb` color mode. For biological images which are often in 
grayscale, one can set `color_mode` to gray as shown below. All other operations will remain the same.

```python
images_list_gray_mode=Segmentation("images/dic", image_suffix ="tif", color_mode = "gray")
show_images(images_list_gray_mode.read_images(), images_list_gray_mode.threshold_images(), number = 4)
```

Result

![Sample Gray](https://github.com/Nelson-Gon/pyautocv/blob/master/sample_results/gray_mode.png?raw=true)


To use a different filter

```python

images_list = Segmentation("images/cats")
show_images(images_list.read_images(), images_list.smooth(mask="median", kernel_shape=(7, 7)))

```

![Cats-Median-Smooth](https://github.com/Nelson-Gon/pyautocv/blob/master/sample_results/cat_median_smooth.png?raw=true)


* Edge Detection 

To detect edges in a directory of images, we can use `Segmentation`'s `detect_edges`. 

```python

show_images(images_list.read_images(), images_list.detect_edges(operator="roberts", mask="gaussian", sigma=0.8))

```

The above will give us the following result


![Sample_colored](https://github.com/Nelson-Gon/pyautocv/blob/master/sample_results/cats_gauss_edge.png?raw=true)


To use a different filter e.g Laplace,

```python

show_images(images_list.read_images(), images_list.detect_edges(operator="laplace", mask="gaussian", sigma=0))

```

This results in

![Laplace](https://github.com/Nelson-Gon/pyautocv/blob/master/sample_results/cats_laplace_gaussian.png?raw=true)



* Thresholding

To perform thresholding, we can use the method `threshold_images`.



```python
to_threshold = Segmentation("images/biology")
show_images(to_threshold.read_images(),to_threshold.threshold_images())

```

![Threshold](https://github.com/Nelson-Gon/pyautocv/blob/master/sample_results/bio_thresh.png?raw=true)

To use a different thresholding method.

```python

show_images(to_threshold.read_images(),to_threshold.threshold_images(threshold_method="otsu"))

```

The above gives us:

![otsu](https://github.com/Nelson-Gon/pyautocv/blob/master/sample_results/bio_thresh_otsu.png?raw=true)

For cat lovers, here's thresholding with inverse binary.

```python

show_images(images_list.read_images(),images_list.threshold_images(threshold_method="binary_inverse"))

```

Result:

![Cats](https://github.com/Nelson-Gon/pyautocv/blob/master/sample_results/cats_bin_inverse.png?raw=true)



Thresholding applied to images of houses.

```python
images_list=Segmentation("images/houses")
show_images(images_list.read_images(), images_list.threshold_images(threshold_method="thresh_to_zero"))
```

![Threshold-Houses](https://github.com/Nelson-Gon/pyautocv/blob/master/sample_results/houses_thresh.png?raw=true)

```python
images_list=Segmentation("images/potholes")
show_images(images_list.read_images(), images_list.threshold_images("binary"))
```

![Potholes](https://github.com/Nelson-Gon/pyautocv/blob/master/sample_results/potholes.png?raw=true)


These and more examples are available in [example.py](https://github.com/Nelson-Gon/pyautocv/blob/1bc67af448ea0bab00ea7223354619f7e9a5d42c/examples/example.py). Image sources are
shown in `sources.md`. If you feel attribution was not made, please file an issue and cite the violating image.




**Citation**

Nelson Gonzabato(2021) pyautocv: (Semi) Automated Image Processing, https://github.com/Nelson-Gon/pyautocv.


```shell
@misc {Gonzabato2021,
author = {Gonzabato, N},
title = {pyautocv: (Semi) Automated Image Processing},
year = {2021},
publisher = {GitHub},
journal = {GitHub repository},
howpublished = {\url{https://github.com/Nelson-Gon/pyautocv}},
commit = {7fe2e0f7894e8be4588a22758e8097c247cd1cd9}

```

>Thank you very much

> “A language that doesn't affect the way you think about programming is not worth knowing.”
― Alan J. Perlis


---

**References**

* [Bebis](https://www.cse.unr.edu/~bebis/CS791E/Notes/EdgeDetection.pdf)

* [Standford, author unknown](https://ai.stanford.edu/~syyeung/cvweb/tutorial3.html)

* [Funkhouser et al.,2013](https://www.cs.princeton.edu/courses/archive/fall13/cos429/lectures/05-segmentation1)
