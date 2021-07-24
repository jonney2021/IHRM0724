# 导包
import json
import unittest
from api.login import LoginAPI
from parameterized import parameterized


# 构建测试数据
def build_data():
    # 指定文件路径
    json_file = "../data/login.json"
    # 打开json文件
    test_data = []
    with open(json_file, encoding="utf-8") as f:
        json_data = json.load(f)
        for case_data in json_data:
            login_data = case_data.get("login_data")
            status_code = case_data.get("status_code")
            success = case_data.get("success")
            code = case_data.get("code")
            message = case_data.get("message")
            test_data.append((login_data, status_code, success, code, message))
            print("test_data = {}".format((login_data, status_code, success, code, message)))
    return test_data


# 创建测试类
class TestLogin(unittest.TestCase):

    # 前置处理
    def setUp(self):
        self.login_api = LoginAPI()

    @parameterized.expand(build_data)
    # 定义测试用例
    def test01_login(self, login_data, status_code, success, code, message):
        # 调用登录接口进行登录
        response = self.login_api.login(login_data)
        print(response.json())

        # 断言
        self.assertEqual(status_code, response.status_code)
        self.assertEqual(success, response.json().get("success"))
        self.assertEqual(code, response.json().get("code"))
        self.assertIn(message, response.json().get("message"))
