# coding:utf-8

import unittest
import time
from HTMLTestReport import HTMLTestRunner

dirpath = './scripts'
discover = unittest.defaultTestLoader.discover(dirpath, pattern='*_tc.py')
currenttime = time.strftime('%y%m%d%H%M%S ')
filedir = './reports/' + 'report' + currenttime + '.html'
fp = open(filedir, 'wb')
runner = HTMLTestRunner(stream=fp, title=u'计算器自动化测试报告', description=u'计算器自动化测试项目详细描述')
runner.run(discover)
fp.close()



'''
file_path = './scripts'
discover = unittest.defaultTestLoader.discover(file_path,pattern='*_tc.py')
runner = unittest.TextTestRunner()
runner.run(discover)
'''