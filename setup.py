from setuptools import setup, find_packages


setup(name='simplecv',
      version=open("simplecv/version.py").read().rstrip(),
      description='(Semi) Automated Image Processing',
      url="http://www.github.com/Nelson-Gon/simplecv",
      download_url="https://github.com/Nelson-Gon/simplecv/archive/v0.1.0.zip",
      author='Nelson Gonzabato',
      author_email='gonzabato@hotmail.com',
      license='MIT',
      keywords="image-data image-analysis computer-vision image-processing",
      packages=find_packages(),
      long_description=open('README.md').read(),
      scripts=['scripts/example.py'],
      long_description_content_type='text/markdown',
      install_requires=['scikit-image', 'scipy', 'matplotlib', 'opencv-python'],
      zip_safe=False,
      python_requires='>=3.6',
      include_package_data=True)
