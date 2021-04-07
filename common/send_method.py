# _*_ coding:utf-8 _*_
# File Name: send_method
# Author： Emily
# Date:  2021/4/6  15:35
# Description : 封装接口请求方法


import requests
import json


class SendMethod:
    """
    请求方式：get、post、put、delete
    请求参数：get/delete：params
            post/put:json
    返回值类型：json
    """

    # 静态方式不需要实例化，使用方式：类名.静态方法
    @staticmethod
    def send_method(method, url, data, params):
        if method == "get" or method == "delete":
            response = requests.request(method=method, url=url, params=params)
        elif method == "post" or method == "put":
            response = requests.request(method=method, url=url, json=data)
        else:
            print("请求方式不正确")
            response = None
        # 如果请求方式是delete，只返回状态码
        if method == "delete":
            return response.status_code
        else:
            return response.json()

    @staticmethod
    def format_response(response):
        """
        :param response: 返回数据
        :return:
        """
        return json.dumps(response, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    url = "http://127.0.0.1:8000/api/departments/"
    method = "get"
    params = {"$dep_id_list": "111,113,112"}
    res = SendMethod.send_method(method, url, None, params)
    print(SendMethod.format_response(res))
    # method = "post"
    # data = {
    #     "data": [
    #         {
    #             "dep_id": "T033",
    #             "dep_name": "T033",
    #             "master_name": "T033",
    #             "slogan": "jT033a"
    #         }
    #     ]
    # }
    # res = SendMethod.send_method(method, url, data)
    # print(SendMethod.format_response(res))
