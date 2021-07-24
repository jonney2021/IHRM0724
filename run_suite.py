# 导包
import time
import unittest
from scripts.test01_login import TestLogin
from scripts.test03_employee import TestEmployee
from tools.HTMLTestRunner import HTMLTestRunner

# 封装测试套件
suite = unittest.TestSuite()
# 登录接口测试用例
suite.addTest(unittest.makeSuite(TestLogin))
# 员工管理场景测试用例
suite.addTest(TestLogin("test01_case001"))   # 解决员工管理接口依赖登录接口问题
suite.addTest(unittest.makeSuite(TestEmployee))
# 指定测试报告的路径
report = "./report/report-{}.html".format(time.strftime("%Y%m%d-%H%M%S"))
# 打开文件流
with open(report,"wb") as f:
    # 创建HTMLTestRunner运行器
    runner = HTMLTestRunner(f,title="API report")
    # 执行测试套件
    runner.run(suite)