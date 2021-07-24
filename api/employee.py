"""
员工添加
员工修改
员工查询
员工删除
"""

# 导包

# 创建接口类
import requests
import app

class EmployeeAPI:
    # 初始化
    def __init__(self):
        self.url_add_employee = app.BASE_URL + "/api/sys/user"
        self.url_update_employee = app.BASE_URL + "/api/sys/user/{}"
        self.url_get_employee = app.BASE_URL + "/api/sys/user/{}"
        self.url_delete_employee = app.BASE_URL + "/api/sys/user/{}"

    # 员工添加
    def add_employee(self,add_employee_data):
        return requests.post(url=self.url_add_employee,json=add_employee_data,headers=app.headers_data)

    # 修改员工
    def update_employee(self, employee_id, update_data):
        url = self.url_update_employee.format(employee_id)
        return requests.put(url=url, json=update_data,headers=app.headers_data)

    # 查询员工
    def get_employee(self,employee_id):
        url = self.url_update_employee.format(employee_id)
        return requests.get(url=url,headers=app.headers_data)

    # 删除员工
    def delete_employee(self,employee_id):
        url = self.url_delete_employee.format(employee_id)
        return requests.delete(url=url,headers=app.headers_data)
# 封装接口