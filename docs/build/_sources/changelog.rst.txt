
pyautocv's change log
=====================

**pyautocv 0.2.1**

**Major Changes**


* 
  ``show_images`` now supports different color maps

* 
  Classes ``Threshold`` and ``EdgeDetection`` were dropped. Support is now through ``Segmentation``

* 
  ``gray_images`` is now a static method. 

**Additions**


* Added support for more detection methods eg Roberts Cross

----

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
