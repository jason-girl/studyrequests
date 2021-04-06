# _*_ coding:utf-8 _*_
# File Name: get_keyword
# Author： Emily
# Date:  2021/4/6  17:10
# Description : 在接口的返回值中，通过关键字获取对应值
# 需要安装一个库：jsonpath   pip install jsonpath
# jsonpath的使用：jsonpath.jsonpath(源数据，jsonpath表达式）
# jsonpath表达式：$..关键字


import jsonpath

# 源数据
# data = {
#   "count": 3,
#   "next": None,
#   "previous": None,
#   "results": [
#     {
#       "dep_id": "111",
#       "dep_name": "测试学院_1",
#       "master_name": "测试1",
#       "slogan": "哈哈哈哈"
#     },
#     {
#       "dep_id": "112",
#       "dep_name": "测试学院_2",
#       "master_name": "测试2",
#       "slogan": "哈哈哈哈"
#     },
#     {
#       "dep_id": "113",
#       "dep_name": "测试学院_3",
#       "master_name": "测试3",
#       "slogan": "哈哈哈哈"
#     }
#   ]
# }

# 根据关键字查找对应的值
# print(jsonpath.jsonpath(data, "$..count")[0])
# 封装通过关键字来获取对应值


class GetKeyword:

  @staticmethod
  def get_value_by_keyword(data, keyword):
    """
    通过关键，获取一组数据
    :param data: 数据源(接口返回值)
    :param keyword: 关键字
    :return:
    """
    return jsonpath.jsonpath(data, f"$..{keyword}")


if __name__ == '__main__':

    data = {
      "count": 3,
      "next": None,
      "previous": None,
      "results": [
        {
          "dep_id": "111",
          "dep_name": "测试学院_1",
          "master_name": "测试1",
          "slogan": "哈哈哈哈"
        },
        {
          "dep_id": "112",
          "dep_name": "测试学院_2",
          "master_name": "测试2",
          "slogan": "哈哈哈哈"
        },
        {
          "dep_id": "113",
          "dep_name": "测试学院_3",
          "master_name": "测试3",
          "slogan": "哈哈哈哈"
        }
      ]
      }
    print(GetKeyword.get_value_by_keyword(data, "master_name"))
