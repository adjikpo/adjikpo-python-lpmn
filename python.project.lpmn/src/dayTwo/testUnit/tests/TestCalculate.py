#coding:utf-8
import sys
sys.path.append('..')
from package.Calculate import Calculate
import unittest


class TestCalculate(unittest.TestCase):
    
    def testAdd(self):
        c = Calculate()
        assert c.add(1,4) == 5

if __name__ == '__main__':
    unittest.main()