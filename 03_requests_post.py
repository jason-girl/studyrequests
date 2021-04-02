# _*_ coding:utf-8 _*_
# File Name: 03_requests_post
# Author： Emily
# Date:  2021/4/1  17:05
# Description : requests库中post请求方式


# 1.导包
import requests
import json

# 2.准备接口三要素
# 请求地址+请求方式
url = "http://127.0.0.1:8000/api/departments/"
# 请求参数
# x-www-form-urlencoded
# data = {
#     "username": "Tom",
#     "password": "123456",
#     "hubby": "Jerry"
# }
# json格式请求参数
data = {
    "data": [
        {
            "dep_id": "44444444",
            "dep_name": "Test学院",
            "master_name": "Test-Master",
            "slogan": "Here is Slogan"
        }
    ]
}
# 发送请求
response = requests.get(url=url, json=data)
# 返回值
print(response)
