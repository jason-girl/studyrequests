# _*_ coding:utf-8 _*_
# File Name: test_add_dep
# Author： Emily
# Date:  2021/4/7  14:45
# Description :

# 测试用例是在unittest框架下编写
import unittest
# 测试添加学院接口
from interface.add_department import AddDepartment
from common.get_keyword import GetKeyword


class TestAddDep(unittest.TestCase):
    def setUp(self) -> None:
        self.add_dep = AddDepartment()

    def test_add_dep(self):
        """ 测试成功添加学院 """
        data = {
                "data": [
                        {
                            "dep_id": "T08",
                            "dep_name": "Test学院",
                            "master_name": "Test-Master",
                            "slogan": "Here is Slogan"
                        }
                  ]
            }
        # 得到新增学院的接口返回值
        response = self.add_dep.add_dep(data)
        # 获取添加成功后的dep_id
        dep_id = GetKeyword.get_value_by_keyword(response["create_success"], "dep_id")
        # 断言实际获取到的dep_id和预期的dep_id做比较
        self.assertEqual(dep_id[0], "T08")
        """
        # 返回值的验证有3种情况
        # 1、添加成功
        # 2、添加id已存在的学院
        # 3、参数错误
        根据多借口文档的分析
        可以通过判断返回值是否包含“status_code”区分1,2和3，然后
        区分1和2；
        根据返回值中already_exist.count是否为0，判断是否添加成功
        """
        # # 条件判断的个数，根据接口文档返回值的情况来决定
        # # 判断status_code是否在返回值键中
        # if "status_code" in response.key():
        #     res = GetKeyword.get_value_by_keyword(response, "status_code")
        # else:
        #     if GetKeyword.get_value_by_keyword(response["already_exist"], "count") == 0:
        #         res = GetKeyword.get_value_by_keyword(response["create_success"], "dep_id")
        #     else:
        #         res = GetKeyword.get_value_by_keyword(response["already_exist"], "dep_id")
        # expect = "预期结果"
        # self.assertEqual(res, expect)


if __name__ == '__main__':
    unittest.main()

