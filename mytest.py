from unittest import TestSuite
from unittest import TextTestRunner
from mm.jhh import MyTest
from HTMLTestRunner_cn import HTMLTestRunner
suite=TestSuite()
suite.addTest((MyTest('test_1')))

#TextTestRunner().run(suite)

with open(r'C:\Users\Administrator\Desktop\aa\a.html','wb') as f:
    HTMLTestRunner(stream=f, title='test', description='mytest').run(suite)