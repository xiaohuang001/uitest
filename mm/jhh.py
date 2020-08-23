import unittest

class MyTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(1,1)

    def test_2(self):
        self.assertEqual(1,2)