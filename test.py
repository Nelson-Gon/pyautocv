# Unit tests for pyautocv
import unittest
from pyautocv.segmentation import *
import os

# Still need to figure out how to automatically set dir
# Use __abspath__ and __realpath__ somehow fail.

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

    def test_errors_are_thrown(self):
        with self.assertRaises(ValueError) as err:
            Segmentation("images/cars", "nope")
        # Check that reading images failed if we change the target format
        self.assertEqual(str(err.exception), "Only png, jpg, and tif are supported")

    def test_graying(self):

        self.assertEqual(len(color_read.shape), 3)
        # If grayed/greyed
        self.assertEqual(len(gray_read.shape), 2)

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


if __name__ == "__main__":
    unittest.main()
