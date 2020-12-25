# Contributing to pyautocv

This document provides guidelines for contributions to pyautocv.

**Kinds of contribution**

* Typo fixes
* Documentation enhancements
* Pull requests


**Fixing typos and enhancing documentation**

To fix typos and/or grammatical errors, please edit the corresponding `.py` or `.md` file that generates the documentation. 

Please also update the docs using `sphinx`

**Pull Requests**

* Please raise an issue for discussion and reproducibility checks at [issues](https://github.com/Nelson-Gon/pyautocv/issues)

* Once the bug/enhancement is approved, please create a Git branch for the pull request.

* Make changes and ensure that builds are passing the necessary checks on Travis.

* Update `changelog.md` to reflect the changes made.

* Do the following:

```

# The Makefile here is Windows specific


cd docs
sphinx-apidoc -o source/ ../pyautocv
# copy changelog and README or get their diff and copy it to docs/source
# Change image paths ie . to ../.. or use direct links to github
# make rst files from md
# Move these to docs/source
# use make on *nix or if you have make on Windows
# Ensure that Make settings point to the right build directory
python -m m2r README.md changelog.md --overwrite && mv README.rst changelog.rst docs/source && ./make.bat html
# check docs
sphinx-build docs/source -W -b linkcheck -d docs/build/doctrees/ docs/build/html/

make latexpdf

```
Please note that the 'pyautocv' project is released with a
[Contributor Code of Conduct](https://github.com/Nelson-Gon/pyautocv/.github/CODE_OF_CONDUCT.md).
By contributing to this project, you agree to abide by its terms.

[See also](https://samnicholls.net/2016/06/15/how-to-sphinx-readthedocs/) for a guide on Sphinx documentation.
