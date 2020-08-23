import mm.uimain as m
import mm.jhh as j
import unittest


suite=unittest.TestSuite()
suite.addTest(j.MyTest('test_1'))
suite.addTest(j.MyTest('test_2'))
suite.addTest(m.MyTest2('test_1'))
suite.addTest(m.MyTest2('test_2'))


if __name__=='__main__':
  with open('my_report.html', 'wb') as f:
    runner = HTMLTestRunner(
      stream=f,
      title='My unit test',
      description='This demonstrates the report output by HTMLTestRunner.'
    )
    runner.run(suite)