# 导包
import time
import unittest
from BeautifulReport import BeautifulReport
from script.test_ihrm_login import TestIHRMLogin
from script.test_ihrm_employee3 import TestIHRMEmployee3


# 组织套件
# [测试用例-导包]
suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestIHRMEmployee3))
suite.addTest(unittest.makeSuite(TestIHRMLogin))

# 测试报告文件名 [更改文件名]
# file_name = 'IHRM员工管理模块测试用例-%s'% time.strftime("%Y%m%d%H%M%S")
file_name = "ihrm"
# 引入BeautifulReport
# description - 用例名称
# log_path - 保存路径
BeautifulReport(suite).report(description='The IHEM Employee Modul Test Report', filename=file_name, log_path='./report')

print("测试增加一行代码后，试试看会不会触发轮询构建")
