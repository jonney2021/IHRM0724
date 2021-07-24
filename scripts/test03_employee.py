# 导包
import unittest
from api.employee import EmployeeAPI
from utils import common_assert


# 创建测试类
class TestEmployee(unittest.TestCase):
    employee_id = None

    # 前置处理
    def setUp(self):
        self.employee_api = EmployeeAPI()

    # 添加员工测试用例设计
    def test01_add_employee(self):
        add_employee_data ={
            "username": "jack0709t3009588 ",   # 用户名唯一
            "mobile": "13312332588",     # 手机号唯一
            "timeOfEntry": "2021-07-17",
            "formOfEmployment": 1,
            "workNumber": "20688",    # 员工ID号唯一
            "departmentName": "销售",
            "departmentId": "1266699057968001024",
            "correctionTime": "2020-07-30T16:00:00.000Z"
        }
        # 获取响应结果
        response = self.employee_api.add_employee(add_employee_data=add_employee_data)
        print(response.json())

        # 断言
        # self.assertEqual(200, response.status_code)
        # self.assertEqual(True, response.json().get("success"))
        # self.assertEqual(10000, response.json().get("code"))
        # self.assertIn("操作成功", response.json().get("message"))
        common_assert(self,response,200,True,10000,"操作成功")

        # 提取员工id
        TestEmployee.employee_id = response.json().get("data").get("id")

    # 修改员工测试用例设计
    def test02_update_employee(self):
        update_employee_data = {"username": "rose0723"}
        # 获取响应结果
        response = self.employee_api.update_employee(TestEmployee.employee_id,update_data=update_employee_data)
        print(response.json())

        # 断言
        common_assert(self,response,200,True,10000,"操作成功")

    # 查询员工测试用例设计
    def test03_get_employee(self):
        # 获取响应结果
        response = self.employee_api.get_employee(TestEmployee.employee_id)
        print(response.json())

        # 断言
        common_assert(self,response,200,True,10000,"操作成功")

    # 删除员工测试用例设计
    def test04_delete_employee(self):
        # 获取响应结果
        response = self.employee_api.delete_employee(TestEmployee.employee_id)
        print(response.json())

        # 断言
        common_assert(self,response,200,True,10000,"操作成功")