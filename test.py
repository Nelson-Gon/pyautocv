# Unit tests for pyautocv
import unittest
from pyautocv.segmentation import *
import os
from unittest import mock

os.chdir(os.path.dirname(os.path.abspath(__file__)))
print("Working in {}".format(os.getcwd()))

use_object = Segmentation("images/cars", "png")
color_read = use_object.read_images()[0]
gray_read = gray_images(use_object.read_images())[0]


class TestModule(unittest.TestCase):

    def test_is_class(self):
        try:
            self.assertIsInstance(use_object, Segmentation)
        except Exception as err:
            self.fail("Failed with the error: {}".format(str(err)))

        with self.assertRaises(NotADirectoryError) as err:
            Segmentation("not a directory", "png")
        self.assertEqual(str(err.exception), "not a directory is not a valid directory in the current path.")

    def test_errors_are_thrown(self):
        with self.assertRaises(ValueError) as err:
            Segmentation("images/cars", "nope")
        # Check that reading images failed if we change the target format
        self.assertEqual(str(err.exception), "Only png, jpg, and tif are supported")

    def test_graying(self):

        self.assertEqual(len(color_read.shape), 3)
        # If grayed/greyed
        self.assertEqual(len(gray_read.shape), 2)

        with self.assertRaises(TypeError) as err:
            gray_images("not a list")

        self.assertEqual(str(err.exception), "Expected a list of images not str")

    def test_smoothing(self):
        with self.assertRaises(ValueError) as err:
            use_object.smooth(mask="nope")
        self.assertEqual(str(err.exception), "mask should be one of mean, median, box, "
                                             "and gaussian")
        with self.assertRaises(TypeError) as err:
            use_object.smooth(mask="mean", kernel_shape=5)
        self.assertEqual(str(err.exception), "Expected a tuple not int")

        # Expect a list if all works as expected
        smoothed = Segmentation("images/dic", "tif", color_mode="gray").smooth(mask="median")
        self.assertIsInstance(smoothed, list)

    def test_thresholding(self):
        with self.assertRaises(ValueError) as err:
            use_object.threshold_images(threshold_method="nope")
        self.assertEqual(str(err.exception), "Thresholding with nope is not supported")

        self.assertNotEqual(use_object.read_images()[1].flat[40], use_object.threshold_images()[1].flat[40])

    def test_edge_detection(self):
        with self.assertRaises(ValueError) as err:
            use_object.detect_edges(operator="gibberish")
        self.assertEqual(str(err.exception),
                         "Edge detection with gibberish not supported.")
        # If edge detecting, then we expect non equality with read images
        # This is not very pretty and there might be a better way, use this for now

        self.assertNotEqual(use_object.read_images()[1].flat[40], use_object.detect_edges()[1].flat[40])
        # Test gray color mode
        use_gray = Segmentation("images/dic", image_suffix="tif", color_mode="gray")
        self.assertNotEqual(use_gray.read_images()[1].flat[40], use_gray.detect_edges()[1].flat[40])

    def test_image_reading(self):
        jpg_png = Segmentation("images/cats", image_suffix="png")
        # Expect length 3 since we have two jpg and one png in images/car
        self.assertEqual(len(jpg_png.read_images()), 3)

        # Should use pil, expect 15
        tif_only = Segmentation("images/dic", image_suffix="tif")
        self.assertEqual(len(tif_only.read_images()), 15)

    # Use mock tests for arguments
    # TODO Revisit mock of show_images
    # """
    # @mock.patch("pyautocv.segmentation.plt")
    # def test_segmentation(self, mock_plt):
    #   use_this = Segmentation("images/cats", "jpg")
    #  show_images(use_this.read_images(), use_this.read_images())
    # mock_plt.subplots.assert_called_once()
    # """


if __name__ == "__main__":
    unittest.main()
