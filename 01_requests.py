# _*_ coding:utf-8 _*_
# File Name: 01_requests
# Author： Emily
# Date:  2021/3/31  16:06
# Description : requests库的基本使用方式


# 1.导包
import requests
import json
# 2.准备接口三要素
# 请求地址+请求方式
url = "http://127.0.0.1:8000/api/departments/"
# 请求参数
# 发送请求
response = requests.get(url=url)
# 返回值
# print(response)
# # 将返回值按照文本形式显示
# print(response.text)
# # 将返回值以json形式显示  对于返回值类型为json格式
# print(response.json())
# # 显示相应状态码
# print(response.status_code)
# # 获取响应头
# print(response.headers)
# # 获取响应源码
# print(response.content)
dict_json = response.json()
# 美化返回结果，返回值数据类型json格式
print(json.dumps(dict_json, indent=2, ensure_ascii=False))
