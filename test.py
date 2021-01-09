# Unit tests for pyautocv
import unittest
from pyautocv.segmentation import *
import os


# Still need to figure out how to automatically set dir
# Use __abspath__ and __realpath__ somehow fail.
def dir_change():
    if os.getcwd() == "pyautocv":
        pass
    else:
        os.chdir("pyautocv")


dir_change()


class TestModule(unittest.TestCase):
    def test_is_class(self):
        try:
            self.assertIsInstance(Segmentation("images/cars", "png"), Segmentation)
        except Exception as err:
            self.fail("Failed with the error: {}".format(str(err)))

    def test_errors_are_thrown(self):
        with self.assertRaises(ValueError) as err:
            my_object = Segmentation("images/cars", "nope")
        # Check that reading images failed if we change the target format
        self.assertEqual(str(err.exception), "Only png, jpg, and tif are supported")


if __name__ == "__main__":
    unittest.main()
