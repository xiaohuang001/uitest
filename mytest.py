from unittest import TestSuite
from unittest import TextTestRunner
from mm.jhh import MyTest

suite=TestSuite()
suite.addTest((MyTest('test_1')))

TextTestRunner().run(suite)

