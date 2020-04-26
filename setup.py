from setuptools import setup, find_packages


setup(name='pyautocv',
      version=open("pyauto/version.py").read().rstrip(),
      description='(Semi) Automated Image Processing',
      url="http://www.github.com/Nelson-Gon/pyautocv",
      download_url="https://github.com/Nelson-Gon/pyautocv/archive/v0.1.1.zip",
      author='Nelson Gonzabato',
      author_email='gonzabato@hotmail.com',
      license='MIT',
      keywords="image-data image-analysis computer-vision image-processing",
      packages=find_packages(),
      long_description=open('README.md').read(),
      scripts=['examples/example.py'],
      long_description_content_type='text/markdown',
      install_requires=['scikit-image', 'scipy', 'matplotlib', 'opencv-python'],
      zip_safe=False,
      python_requires='>=3.6',
      include_package_data=True)
