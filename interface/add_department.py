# _*_ coding:utf-8 _*_
# File Name: add_department
# Author： Emily
# Date:  2021/4/7  11:00
# Description : 添加学院

from common.send_method import SendMethod
from common.get_keyword import GetKeyword


class AddDepartment:
    def __init__(self, method="post"):
        self.url = "http://127.0.0.1:8000/api/departments/"
        self.method = method

    def add_dep(self, data):
        """ 请求新增学员接口，针对单接口测试"""
        response = SendMethod.send_method(self.method, self.url, data, None)
        return response

    def get_depid(self, data):
        """ 获取dep_id, 为关联接口测试准备"""
        response = self.add_dep(data)
        # 获取新增学员接口返回值中的dep_id
        dep_id = GetKeyword.get_value_by_keyword(response["create_success"], "dep_id")
        return dep_id


if __name__ == '__main__':
    data = {
        "data": [
            {
                "dep_id": "133333",
                "dep_name": "133333",
                "master_name": "T033",
                "slogan": "jT033a"
            }
        ]
    }
    print(AddDepartment().add_dep(data))
