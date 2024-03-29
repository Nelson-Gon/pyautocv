# pyautocv's change log 

**Version 0.3.1**

* Due to changes in `matplotlib`'s requirements, we now require python greater than or equal to 3.7. 

* We now use `pytest` for testing. This is mostly a developer focused issue.

* Package can now be run at the command line or Terminal via `python -m pyautocv`. 

**Release 0.3.0**



- Extended tests and coverage

- Initial support for action based script run.

- Extended script to make it a bit more flexible 

- Extended the script to handle thresholding, edge detection, and smoothing. 

- Initial support for thresholding scripts. Added arguments to the sample script 

- An `example_script.py` file was added to test running files at the command line

- `titles` was renamed to `custom_titles` in `show_images`

- `show_images` now supports showing only a single list of images

- `plot_hist` is a new function that allows one to plot histograms of images. 

- `stack_images` is a new function that allows one to stack images vertically and horizontally.

- `show_images` now has a `titles` argument to add titles to `plots`.  

- Fixed issues with `read_images` not reading mixed formats. 

- `reshape_images` and `resize_images` are helper functions that were originally written for
[cytounet](https://github.com/Nelson-Gon/cytounet)

- `read_images` now provides a naturally sorted list at least for tiff images. 

- Made `show_images` more flexible regarding the size of the figure shown. 

- Fixed an issue with reading `.tif` images

- `show_images` now shows image side by side which is more intuitive. 

- Added support for different color modes i.e. either grayscale or rgb images

- Added support for tiff(`.tif`) images

- `show_images` is now more customizable with respect to the number of images one would like to show. 

**pyautocv 0.2.1**

**Major Changes**

* `show_images` now supports different color maps

* Classes `Threshold` and `EdgeDetection` were dropped. Support is now through `Segmentation`

* `gray_images` is now a static method. 

**Additions**

* Added support for more detection methods e.g. Roberts Cross

----
**pyautocv 0.2.0**

**Major Additions**
* Class EdgeDetection that inherits from class Segmentation

* Class Threshold specifically for thresholding. This also inherits from Segmentation.

* Added filtering methods

**Major Changes**

* Method `show_images` is now a `static` method.

* `read_images` now supports `png`

* Thresholding is now built on top of opencv. This may change in the future 