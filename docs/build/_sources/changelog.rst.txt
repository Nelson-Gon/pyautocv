
Changes to pyautocv
===================

**pyautocv 0.2.0**

**Major Additions**


* 
  Class EdgeDetection that inherits from class Segmentation

* 
  Class Threshold specifically for thresholding. This also inherits from Segmentation.

* 
  Added filtering methods

**Major Changes**


* 
  Method ``show_images`` is now a ``static`` method.

* 
  ``read_images`` now supports ``png``

* 
  Thresholding is now built on top of opencv. This may change in the future 
