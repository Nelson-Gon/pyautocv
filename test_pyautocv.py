import pytest
from pyautocv.segmentation import *
import os
from unittest import mock


dir_path = os.path.dirname(os.path.abspath(__file__))

def make_path(use_path):
    return os.path.join(dir_path, use_path)

@pytest.fixture 
def test_object():
    def _test_object(dir_path, image_suffix = "png", **kwargs):
        return Segmentation(directory = make_path(dir_path), image_suffix= image_suffix,  **kwargs)
    return _test_object    

def assert_instance(test_object):
    # Very basic assertion. For whatever reason we fail to find tests when using parametrize 
    assert isinstance(test_object(dir_path="images/cats"), Segmentation)

def test_not_object(test_object):
    with pytest.raises(NotADirectoryError, match = "not a directory is not a valid directory in the current path.") as err:
        test_object(dir_path = "not a directory", image_suffix = "png")


def test_error_throws(test_object):
    with pytest.raises(ValueError, match = "Only png, jpg, and tif are supported" ) as err:
        test_object(dir_path = "images/cars", image_suffix = "nope")

# TODO: Use a recursive fixture for this 
def test_graying(test_object):
    use_obj = test_object(dir_path="images/cats").read_images()
    grayed = gray_images(use_obj)
    assert len(use_obj[0].shape) == 3
    # drop extra color index after graying for the first image 
    assert len(grayed[0].shape) == 2

# No fixture needed here 
def test_gray_fails():
    with pytest.raises(TypeError, match = "Expected a list of images not str") as err:
        gray_images("not a list")

def test_smoothing(test_object):
    with pytest.raises(ValueError, match = "mask should be one of mean, median, box, and gaussian") as err:
        test_object(dir_path = "images/cats").smooth(mask="nope")

    with pytest.raises(TypeError, match = "Expected a tuple not int") as err:
        test_object(dir_path = "images/cats").smooth(mask = "mean", kernel_shape = 5) 
    # Expect a list if all works as expected
    smoothed = test_object(dir_path = "images/dic", image_suffix = "tif",
                             color_mode="gray").smooth(mask="median")
    # TODO: use more meaningful tests not just a list instance                              
    assert isinstance(smoothed, list)

def test_thresholding(test_object):
    with pytest.raises(ValueError, match = "Thresholding with nope is not supported") as err:
        test_object(dir_path="images/cats").threshold_images(threshold_method="nope")

    use_object = test_object(dir_path="images/cats")
    assert use_object.read_images()[1].flat[40] !=  use_object.threshold_images()[1].flat[40]


def test_edge_detection(test_object):
    with pytest.raises(ValueError, match = "Edge detection with gibberish not supported." ) as err:
        test_object(dir_path="images/cats").detect_edges(operator="gibberish")
    # If edge detecting, then we expect non equality with read images
    # This is not very pretty and there might be a better way, use this for now
    use_object = test_object(dir_path="images/cats")
    assert use_object.read_images()[1].flat[40] != use_object.detect_edges()[1].flat[40]
    # Test gray color mode
    use_gray = Segmentation(directory = make_path("images/dic"), image_suffix="tif", color_mode="gray")
    assert use_gray.read_images()[1].flat[40] != use_gray.detect_edges()[1].flat[40]
    # Test that if we provide sub-folders we get the expected image length
    assert len(use_object.read_images(other_directory = make_path("images/cats"))) == 6
 
def test_image_reading(test_object):
    # Expect length 3 since we have two jpg and one png in images/car
    assert len(test_object(dir_path="images/cats").read_images()) == 3
    # Should use pil, expect 15
    tif_only = test_object(dir_path = "images/dic", image_suffix="tif")
    assert len(tif_only.read_images()) == 15

   

def test_resizing(test_object):
    use_object = test_object(dir_path="images/cats")
    resized = resize_images(use_object.read_images(), (125, 125))
    assert resized[0].shape[0] == 125
    with pytest.raises(TypeError, match ="Expected a tuple in target_size not int") as err:
        resize_images(use_object.read_images(), 4)
    with pytest.raises(ValueError, match = "Please provide both an image list and a target size") as err:
        resize_images()

def test_reshaping(test_object):
    use_object = test_object(dir_path="images/cats")
    with pytest.raises(ValueError, match ="Please provide a list of images to reshape.") as err:
        reshape_images()
    # Check that reshaped images are not the same shape as original images
    reshaped = reshape_images(use_object.read_images())
    assert reshaped[0].shape ==  use_object.read_images()[0].shape


def test_stacking(test_object):
    use_object = test_object(dir_path="images/cats")
    with pytest.raises(ValueError, match = "Please provide two lists to stack") as err:
        stack_images()
    with pytest.raises(TypeError, match ="Both list_one and list_two should be lists" ) as err:
        stack_images(use_object.read_images(), "gibberish")

    with pytest.raises(ValueError, match = "direction should be one of horizontal, vertical, h, v not gibberish") as err:
        stack_images(use_object.read_images(), use_object.threshold_images(),
                        direction="gibberish")
    assert len(stack_images(use_object.read_images(), use_object.read_images())) == 3

# TODO: Mocks 
# @mock.patch("pyautocv.segmentation.plt")
# def test_hist_plots(use_object, mock_plt):
#     image_test = use_object.read_images()[1]
#     plot_hist(image_test)
#     mock_plt.plot.assert_called_once()
#     # TODO assert that color_mode works as expected
#     mock_plt.xlim.assert_called_once_with([0, 256])

# # TODO: Figure out why this only fails as a test.
# @pytest.mark.xfail 
# @mock.patch("pyautocv.segmentation.plt")
# def test_show_images(use_object, mock_plt):
#     show_images(use_object.read_images(), use_object.read_images())
#     mock_plt.subplots.assert_called_once()




# TODO: Restore these 
# class TestModule(unittest.TestCase):

#     def test_is_class(self):
#         try:
#             self.assertIsInstance(use_object, Segmentation)
#         except Exception as err:
#             self.fail("Failed with the error: {}".format(str(err)))

#         with self.assertRaises(NotADirectoryError) as err:
#             Segmentation("not a directory", "png")
#         self.assertEqual(str(err.exception), "not a directory is not a valid directory in the current path.")

    # def test_errors_are_thrown(self):
    #     with self.assertRaises(ValueError) as err:
    #         Segmentation(cars, "nope")
    #     # Check that reading images failed if we change the target format
    #     self.assertEqual(str(err.exception), "Only png, jpg, and tif are supported")


  

   









