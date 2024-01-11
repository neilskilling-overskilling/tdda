import os
from setuptools import setup

# The zip_safe setting should not be required as it is set in pyproject.toml 
# but otherwise we get a bad marshal data error
setup(zip_safe=False)