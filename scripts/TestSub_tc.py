# coding:utf-8
import unittest
from Calc import Calculation

@unittest.skipUnless(False,'')
class TestSub(unittest.TestCase):
    u'''减法运算功能验证'''
    def setUp(self):
        print('用例开始执行！')
        self.obj_sub = Calculation()
    def tearDown(self):
        print('用例执行结束！')

    @unittest.skipUnless(True,'')
    def testSub001(self):
        u'''整数相减功能验证'''
        r = self.obj_sub.sub(3,4)
        self.assertEqual(r,-1)

    @unittest.skipUnless(True,'')
    def testSub002(self):
        u'''小数相减功能验证'''
        r = self.obj_sub.sub(3.1,4.7)
        self.assertEqual(r,-1.6)

    @unittest.skipUnless(True,'')
    def testSub003(self):
        u'''负数相减功能验证'''
        r = self.obj_sub.sub(-3,-4)
        self.assertEqual(r,1)

if __name__ == '__main__':
    unittest.main()