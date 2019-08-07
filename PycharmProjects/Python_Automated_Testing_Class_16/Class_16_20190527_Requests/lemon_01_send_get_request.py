import requests

# 构造url
url = 'http://test.lemonban.com:8080/futureloan/mvc/api/member/register'
# 创建请求参数
params = {
    "mobilephone": "18600001111",
    "pwd": "654321",
    "nickname": "dranson"
}
# 向服务器发起get请求
resp = requests.get(url, params=params)
# 获取状态码
print(resp.status_code)
# 获取响应体数据（str）
print(resp.text)
# 获取json格式数据转换成的字典
print(resp.json())
# 获取cookie
print(resp.cookies)  # cookies类似于字典，支持字典所有操作

pass
