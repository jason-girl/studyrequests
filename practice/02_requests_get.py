# _*_ coding:utf-8 _*_
# File Name: 02_requests_get
# Author： Emily
# Date:  2021/3/31  17:41
# Description : requests库中get请求方式

# 1.导包
import requests
import json
# 2.准备接口三要素
# 请求地址+请求方式
url = "http://127.0.0.1:8000/api/departments/"
# 请求参数--字典格式数据
data = {"$dep_id_list": "17,19,20"}
# 发送请求
response = requests.get(url=url, params=data)
# 美化返回结果，返回值数据类型json格式
res = json.dumps(response.json(), indent=2, ensure_ascii=False)
print(res)
