# coding:utf-8
import unittest
from Calc import Calculation

@unittest.skipUnless(True,'')
class TestAdd(unittest.TestCase):
    u'''加法运算功能验证'''
    def setUp(self):
        print('用例开始执行！')
        self.obj_add = Calculation()
    def tearDown(self):
        print('用例执行结束！')

    @unittest.skipUnless(True, '')
    def testAdd001(self):
        u'''整数相加功能验证'''
        r = self.obj_add.add(3,4)
        self.assertEqual(r,7)

    @unittest.skipUnless(True, '')
    def testAdd002(self):
        u'''小数相加功能验证'''
        r = self.obj_add.add(3.1,4.7)
        self.assertEqual(r,7.8)

    @unittest.skipUnless(True, '')
    def testAdd003(self):
        u'''负数相加功能验证'''
        r = self.obj_add.add(-3,-4)
        self.assertEqual(r,-7)

if __name__ == '__main__':
    unittest.main()