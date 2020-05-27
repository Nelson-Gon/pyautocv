
**(Semi) Automated Image Processing**


.. image:: https://www.repostatus.org/badges/latest/wip.svg
   :target: https://www.repostatus.org/badges/latest/wip.svg
   :alt: Stage
 
.. image:: https://zenodo.org/badge/DOI/10.5281/zenodo.3766956.svg
   :target: https://doi.org/10.5281/zenodo.3766956
   :alt: DOI


.. image:: https://github.com/Nelson-Gon/pyautocv/workflows/Test-Package/badge.svg
   :target: https://github.com/Nelson-Gon/pyautocv/workflows/Test-Package/badge.svg
   :alt: Test-Package


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
   :alt: PyPI download Month


.. image:: https://img.shields.io/pypi/dw/pyautocv.svg
   :target: https://pypi.python.org/pypi/pyautocv/
   :alt: PyPI download week


.. image:: https://img.shields.io/pypi/dd/pyautocv.svg
   :target: https://pypi.python.org/pypi/pyautocv/
   :alt: PyPI download day


.. image:: https://img.shields.io/badge/Maintained%3F-yes-green.svg
   :target: https://GitHub.com/Nelson-Gon/pyautocv/graphs/commit-activity
   :alt: Maintenance


.. image:: https://img.shields.io/github/last-commit/Nelson-Gon/pyautocv.svg
   :target: https://github.com/Nelson-Gon/pyautocv/commits/master
   :alt: GitHub last commit


.. image:: https://img.shields.io/badge/Made%20with-Python-1f425f.svg
   :target: https://www.python.org/
   :alt: made-with-python


.. image:: https://img.shields.io/github/issues/Nelson-Gon/pyautocv.svg
   :target: https://GitHub.com/Nelson-Gon/pyautocv/issues/
   :alt: GitHub issues


.. image:: https://img.shields.io/github/issues-closed/Nelson-Gon/pyautocv.svg
   :target: https://GitHub.com/Nelson-Gon/pyautocv/issues?q=is%3Aissue+is%3Aclosed
   :alt: GitHub issues-closed


.. image:: https://img.shields.io/badge/license-MIT-blue.svg
   :target: https://github.com/Nelson-Gon/pyautocv/blob/master/LICENSE
   :alt: license


**Project Aims**

The goal of pyautocv is to provide a simple computer vision(cv) workflow that enables one to automate 
or at least reduce the time spent in image (pre)-processing. 

**Installing the package**

From pypi:

.. code-block::


   pip install pyautocv

From GitHub

.. code-block::

   pip install pip install git+https://github.com/Nelson-Gon/pyautocv.git
   #or
   # clone the repo
   git clone https://www.github.com/Nelson-Gon/pyautocv.git
   cd pyautocv
   python3 setup.py install

**Available Class**


* 
  Segmentation is a super class on which other classes build

* 
  EdgeDetection is dedicated to edge detection. Currently supported kernels are stored in ``.available_operators()``

* 
  Thresholding dedicated to thresholding.

**Example Usage**


* Smoothing

To smooth a directory of images, we can use ``EdgeDetection``\ 's ``smooth`` method as
follows:

.. code-block:: python

   from pyautocv.segmentation import *
   to_smooth = EdgeDetection("images/people","sobel_vertical")
   show_images(*[to_smooth.gray_images(), to_smooth.smooth()])

This will give us:


.. image:: sample_results/people_smooth.png
   :target: sample_results/people_smooth.png
   :alt: Smoothened



* Edge Detection 

To detect edges in a directory image, we provide original(grayed) images for comparison to
images that have been transformed to detect edges. 

.. code-block:: python


   edge_detection = EdgeDetection("images","sobel_vertical")
   # use a gaussian blur
   # detect edges with sobel_vertical
   show_images(edge_detection.read_images(), edge_detection.detect_edges(operator="sobel_vertical",mask="gaussian",sigma=3.5))

The above will give us the following result:


.. image:: ./sample_results/sample_sobel_gaussian.png
   :target: ./sample_results/sample_sobel_gaussian.png
   :alt: Sample_colored


To use a different filter e.g Laplace,

.. code-block::


   show_images(edge_detection.read_images(), edge_detection.detect_edges(operator="laplace",mask="gaussian",sigma=3.5))

This results in:


.. image:: ./sample_results/gauss_laplace.png
   :target: ./sample_results/gauss_laplace.png
   :alt: Laplace



* Thresholding

To perform thresholding, we can use ``Threshold``\ 's methods dedicated to thresholding.

We use flowers as an example:

.. code-block::

   to_threshold = Threshold("images/biology",threshold_method="binary")
   show_images(to_threshold.read_images(),to_threshold.threshold_images())
   # cats
   to_threshold_cats = Threshold("images/cats",threshold_method="binary")
   show_images(to_threshold_cats.read_images(),to_threshold_cats.threshold_images())
   #potholes
   to_threshold = Threshold("images/potholes",threshold_method="otsu")
   show_images(to_threshold.read_images(),to_threshold.threshold_images())
   # houses
   to_threshold = Threshold("images/houses",threshold_method="binary_inverse")
   show_images(to_threshold.read_images(),to_threshold.threshold_images())


.. image:: ./sample_results/bio_new.png
   :target: ./sample_results/bio_new.png
   :alt: Biology



.. image:: ./sample_results/cats_example.png
   :target: ./sample_results/cats_example.png
   :alt: cats



.. image:: ./sample_results/potholes_sample.png
   :target: ./sample_results/potholes_sample.png
   :alt: Potholes



.. image:: ./sample_results/houses_bin_inverse.png
   :target: ./sample_results/houses_bin_inverse.png
   :alt: Houses


These and more examples are available in `example2.py <./examples/example2.py>`_. Image sources are
shown in ``sources.md``. If you feel, attribution was not made, please file an issue
and cite the violating image.

..

   Thank you very much

   “A language that doesn't affect the way you think about programming is not worth knowing.”
   ― Alan J. Perlis


----

References:


* 
  `Bebis <https://www.cse.unr.edu/~bebis/CS791E/Notes/EdgeDetection.pdf>`_

* 
  `Standford, author unknown <https://ai.stanford.edu/~syyeung/cvweb/tutorial3.html>`_

* 
  `Funkhouser et al.,2013 <https://www.cs.princeton.edu/courses/archive/fall13/cos429/lectures/05-segmentation1>`_
