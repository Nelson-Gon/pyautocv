from setuptools import setup, find_packages
from pyautocv.version import __version__
zip_link = "https://github.com/Nelson-Gon/pyautocv/archive/refs/tags/v"+__version__+".zip"
setup(name='pyautocv',
      version=__version__,
      description='(Semi) Automated Image Processing',
      download_url=zip_link,
      url='http://www.github.com/Nelson-Gon/pyautocv',
      author='Nelson Gonzabato',
      author_email='gonzabato@hotmail.com',
      license='MIT',
      keywords="image-data image-analysis computer-vision image-processing",
      packages=find_packages(),
      long_description=open('README.md', encoding="UTF-8").read(),
      long_description_content_type='text/markdown',
      install_requires=['scikit-image', 'scipy', 'matplotlib', 'opencv-python'],
      zip_safe=False,
      python_requires='>=3.7',
      include_package_data=True)
