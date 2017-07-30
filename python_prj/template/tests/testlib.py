"""Provides a library to aid testing."""

##==============================================================#
## SECTION: Imports                                             #
##==============================================================#


import os.path as op
import sys
import unittest

# Allows development version of library to be used instead of installed.
prjdir = op.normpath(op.join(op.abspath(op.dirname(__file__)), r"../{{prj_type}}"))
sys.path.insert(0, prjdir)

##==============================================================#
## SECTION: Class Definitions                                   #
##==============================================================#

class BaseTest(unittest.TestCase):
    def tearDown(test):
        super(BaseTest, test).tearDown()
        # TODO: Additional logic here.
