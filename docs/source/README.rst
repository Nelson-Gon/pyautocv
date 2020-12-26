
(Semi) Automated Image Processing with pyautocv
===============================================


.. image:: https://www.repostatus.org/badges/latest/active.svg
   :target: https://www.repostatus.org/badges/latest/active.svg
   :alt: Stage
 
.. image:: https://zenodo.org/badge/DOI/10.5281/zenodo.3766956.svg
   :target: https://doi.org/10.5281/zenodo.3766956
   :alt: DOI


.. image:: https://github.com/Nelson-Gon/pyautocv/workflows/Test-Package/badge.svg
   :target: https://github.com/Nelson-Gon/pyautocv/workflows/Test-Package/badge.svg
   :alt: Test-Package


.. image:: https://img.shields.io/badge/license-MIT-blue.svg
   :target: https://github.com/Nelson-Gon/pyautocv/blob/master/LICENSE
   :alt: license


.. image:: https://readthedocs.org/projects/pyautocv/badge/?version=latest
   :target: https://pyautocv.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status


.. image:: https://travis-ci.com/Nelson-Gon/pyautocv.svg?branch=master
   :target: https://travis-ci.com/Nelson-Gon/pyautocv.svg?branch=master
   :alt: Travis Build


.. image:: https://badge.fury.io/py/pyautocv.svg
   :target: https://pypi.python.org/pypi/pyautocv/
   :alt: PyPI version fury.io


.. image:: https://img.shields.io/pypi/l/pyautocv.svg
   :target: https://pypi.python.org/pypi/pyautocv/
   :alt: PyPI license


.. image:: https://img.shields.io/pypi/dm/pyautocv.svg
   :target: https://pypi.python.org/pypi/pyautocv/
   :alt: PyPI Downloads Month


.. image:: https://img.shields.io/badge/Maintained%3F-yes-green.svg
   :target: https://GitHub.com/Nelson-Gon/pyautocv/graphs/commit-activity
   :alt: Maintenance


.. image:: https://img.shields.io/github/last-commit/Nelson-Gon/pyautocv.svg
   :target: https://github.com/Nelson-Gon/pyautocv/commits/master
   :alt: GitHub last commit


.. image:: https://img.shields.io/github/issues/Nelson-Gon/pyautocv.svg
   :target: https://GitHub.com/Nelson-Gon/pyautocv/issues/
   :alt: GitHub issues


.. image:: https://img.shields.io/github/issues-closed/Nelson-Gon/pyautocv.svg
   :target: https://GitHub.com/Nelson-Gon/pyautocv/issues?q=is%3Aissue+is%3Aclosed
   :alt: GitHub issues-closed


**Project Aims**

The goal of ``pyautocv`` is to provide a simple computer vision(cv) workflow that enables one to automate 
or at least reduce the time spent in image (pre)-processing. 

**Installing the package**

From PyPI

.. code-block:: shell


   pip install pyautocv

From GitHub

.. code-block:: shell

   pip install git+https://github.com/Nelson-Gon/pyautocv.git
   #or
   # clone the repo
   git clone https://www.github.com/Nelson-Gon/pyautocv.git
   cd pyautocv
   python3 setup.py install

**Example Usage**

**Note**\ : Although these methods can be run via this script, the script is less flexible and might be useful for quick
exploration but not extended analysis. 

To run the script at the  commandline, we can do the following

.. code-block:: shell


   # Ensure you have your paths set well
   # This assumes that we are inside the package's top level directory

    python scripts/processing.py -d "images/cats" -s "png" -m "binary_inverse" -o "threshold" -mt 250 -t 50

Sample Result


.. image:: https://github.com/Nelson-Gon/pyautocv/blob/master/sample_results/sample_script.png?raw=true
   :target: https://github.com/Nelson-Gon/pyautocv/blob/master/sample_results/sample_script.png?raw=true
   :alt: Command Line Script


To perform edge detection

.. code-block:: shell


   python scripts/processing.py -d "images/biology" -s "jpg" -o "detect_edges" -m "sobel_vertical" -k 3


.. image:: https://github.com/Nelson-Gon/pyautocv/blob/master/sample_results/bioscript.png?raw=true
   :target: https://github.com/Nelson-Gon/pyautocv/blob/master/sample_results/bioscript.png?raw=true
   :alt: Bio Script


To smooth images

.. code-block:: shell

   python scripts/processing.py -d "images/houses" -s "jpg" -o "smooth" -m "gaussian" -k 5 5 --sigma 0.7


.. image:: https://github.com/Nelson-Gon/pyautocv/blob/master/sample_results/houses_smooth.png?raw=true
   :target: https://github.com/Nelson-Gon/pyautocv/blob/master/sample_results/houses_smooth.png?raw=true
   :alt: Houses Smooth


To get help

.. code-block:: shell


   python scripts/processing.py -h

Further exploration is left to the user.

----

The following section shows how to use the more flexible class/methods approach


* Image Gra(e)ying

To grey an image directory

.. code-block:: python

   from pyautocv.segmentation import *

   images_list=Segmentation("images/cats")
   show_images(gray_images(images_list.read_images()), images_list.read_images(), number=2)


.. image:: https://github.com/Nelson-Gon/pyautocv/blob/master/sample_results/cats_gray.png?raw=true
   :target: https://github.com/Nelson-Gon/pyautocv/blob/master/sample_results/cats_gray.png?raw=true
   :alt: Grayed



* Smoothing

To smooth a directory of images, we can use ``EdgeDetection``\ 's ``smooth`` method as
follows

.. code-block:: python


   from pyautocv.segmentation import *

   images_list=Segmentation("images/cats")
   show_images(images_list.smooth(), images_list.read_images(),number=2)

This will give us


.. image:: https://github.com/Nelson-Gon/pyautocv/blob/master/sample_results/cats_smooth.png?raw=true
   :target: https://github.com/Nelson-Gon/pyautocv/blob/master/sample_results/cats_smooth.png?raw=true
   :alt: Smooth


The above uses default parameters including an ``rgb`` color mode. For biological images which are often in 
grayscale, one can set ``color_mode`` to gray as shown below. All other operations will remain the same.

.. code-block:: python

   images_list_gray_mode=Segmentation("images/dic", image_suffix ="tif", color_mode = "gray")
   show_images(images_list_gray_mode.read_images(), images_list_gray_mode.threshold_images(), number = 4)

Result


.. image:: https://github.com/Nelson-Gon/pyautocv/blob/master/sample_results/gray_mode.png?raw=true
   :target: https://github.com/Nelson-Gon/pyautocv/blob/master/sample_results/gray_mode.png?raw=true
   :alt: Sample Gray


To use a different filter

.. code-block:: python


   images_list = Segmentation("images/cats")
   show_images(images_list.read_images(), images_list.smooth(mask="median", kernel_shape=(7, 7)))


.. image:: https://github.com/Nelson-Gon/pyautocv/blob/master/sample_results/cat_median_smooth.png?raw=true
   :target: https://github.com/Nelson-Gon/pyautocv/blob/master/sample_results/cat_median_smooth.png?raw=true
   :alt: Cats-Median-Smooth



* Edge Detection 

To detect edges in a directory of images, we can use ``Segmentation``\ 's ``detect_edges``. 

.. code-block:: python


   show_images(images_list.read_images(), images_list.detect_edges(operator="roberts", mask="gaussian", sigma=0.8))

The above will give us the following result


.. image:: https://github.com/Nelson-Gon/pyautocv/blob/master/sample_results/cats_gauss_edge.png?raw=true
   :target: https://github.com/Nelson-Gon/pyautocv/blob/master/sample_results/cats_gauss_edge.png?raw=true
   :alt: Sample_colored


To use a different filter e.g Laplace,

.. code-block:: python


   show_images(images_list.read_images(), images_list.detect_edges(operator="laplace", mask="gaussian", sigma=0))

This results in


.. image:: https://github.com/Nelson-Gon/pyautocv/blob/master/sample_results/cats_laplace_gaussian.png?raw=true
   :target: https://github.com/Nelson-Gon/pyautocv/blob/master/sample_results/cats_laplace_gaussian.png?raw=true
   :alt: Laplace



* Thresholding

To perform thresholding, we can use the method ``threshold_images``.

.. code-block:: python

   to_threshold = Segmentation("images/biology")
   show_images(to_threshold.read_images(),to_threshold.threshold_images())


.. image:: https://github.com/Nelson-Gon/pyautocv/blob/master/sample_results/bio_thresh.png?raw=true
   :target: https://github.com/Nelson-Gon/pyautocv/blob/master/sample_results/bio_thresh.png?raw=true
   :alt: Threshold


To use a different thresholding method.

.. code-block:: python


   show_images(to_threshold.read_images(),to_threshold.threshold_images(threshold_method="otsu"))

The above gives us:


.. image:: https://github.com/Nelson-Gon/pyautocv/blob/master/sample_results/bio_thresh_otsu.png?raw=true
   :target: https://github.com/Nelson-Gon/pyautocv/blob/master/sample_results/bio_thresh_otsu.png?raw=true
   :alt: otsu


For cat lovers, here's thresholding with inverse binary.

.. code-block:: python


   show_images(images_list.read_images(),images_list.threshold_images(threshold_method="binary_inverse"))

Result:


.. image:: https://github.com/Nelson-Gon/pyautocv/blob/master/sample_results/cats_bin_inverse.png?raw=true
   :target: https://github.com/Nelson-Gon/pyautocv/blob/master/sample_results/cats_bin_inverse.png?raw=true
   :alt: Cats


Thresholding applied to images of houses.

.. code-block:: python

   images_list=Segmentation("images/houses")
   show_images(images_list.read_images(), images_list.threshold_images(threshold_method="thresh_to_zero"))


.. image:: https://github.com/Nelson-Gon/pyautocv/blob/master/sample_results/houses_thresh.png?raw=true
   :target: https://github.com/Nelson-Gon/pyautocv/blob/master/sample_results/houses_thresh.png?raw=true
   :alt: Threshold-Houses


.. code-block:: python

   images_list=Segmentation("images/potholes")
   show_images(images_list.read_images(), images_list.threshold_images("binary"))


.. image:: https://github.com/Nelson-Gon/pyautocv/blob/master/sample_results/potholes.png?raw=true
   :target: https://github.com/Nelson-Gon/pyautocv/blob/master/sample_results/potholes.png?raw=true
   :alt: Potholes


These and more examples are available in `example.py <https://github.com/Nelson-Gon/pyautocv/blob/1bc67af448ea0bab00ea7223354619f7e9a5d42c/examples/example.py>`_. Image sources are
shown in ``sources.md``. If you feel attribution was not made, please file an issue and cite the violating image.

**Citation**

Nelson Gonzabato(2020) pyautocv: (Semi) Automated Image Processing, https://github.com/Nelson-Gon/pyautocv.

.. code-block:: shell

   @misc {Gonzabato2020,
   author = {Gonzabato, N},
   title = {pyautocv: (Semi) Automated Image Processing},
   year = {2020},
   publisher = {GitHub},
   journal = {GitHub repository},
   howpublished = {\url{https://github.com/Nelson-Gon/pyautocv}},
   commit = {2a5a8c48fd91c719d526ed013b298d560df9b73f}

..

   Thank you very much

   “A language that doesn't affect the way you think about programming is not worth knowing.”
   ― Alan J. Perlis


----

**References**


* 
  `Bebis <https://www.cse.unr.edu/~bebis/CS791E/Notes/EdgeDetection.pdf>`_

* 
  `Standford, author unknown <https://ai.stanford.edu/~syyeung/cvweb/tutorial3.html>`_

* 
  `Funkhouser et al.,2013 <https://www.cs.princeton.edu/courses/archive/fall13/cos429/lectures/05-segmentation1>`_
