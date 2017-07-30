##==============================================================#
## SECTION: Imports                                             #
##==============================================================#

from os.path import isfile
from setuptools import setup, find_packages

##==============================================================#
## SECTION: Main Body                                           #
##==============================================================#

setup(
    name = "{{short_name}}",
    version = "0.1.0",
    author = "{{author}}",
    author_email = "{{email}}",
    description = "{{desc}}",
    license = "MIT",
    keywords = "{{keywords}}",
    url = "{{website}}",
    long_description=open("README.rst").read() if isfile("README.rst") else "",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3"
    ],
)
