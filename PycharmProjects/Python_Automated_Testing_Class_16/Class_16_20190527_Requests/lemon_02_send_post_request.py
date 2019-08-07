import requests

# 构造url
url = 'http://test.lemonban.com:8080/futureloan/mvc/api/member/register'
# 创建请求参数
params = {
    "mobilephone": "18600001111",
    "pwd": "654321",
    "nickname": "dranson"
}

json_params = '{"mobilephone": "18600001111", "pwd": "654321", "nickname": "dranson"}'

headers = {
    'user-agent': 'Mozilla/5.0 ljs/1.0'
}

# 向服务器发起post请求
# resp = requests.post(url, params=params)

# 将参数放在请求体，将data传参，会使用x-www-form-urlencoded形式来传参，且会放在请求体中
# resp = requests.post(url, data=params)

# data可以传json格式数据，自动转为字典，但必须符合请求格式，不然没有请求头没有Content-Type
# resp = requests.post(url, data=json_params)

# 使用json格式传参
resp = requests.post(url, json=json_params, headers=headers)

# 获取响应头信息
print(resp.headers)

