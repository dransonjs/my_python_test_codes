import requests

# 构造url
login_url = 'http://test.lemonban.com:8080/futureloan/mvc/api/member/login'
recharge_url = 'http://test.lemonban.com:8080/futureloan/mvc/api/member/recharge'
# 创建请求参数
login_params = {
    "mobilephone": "18600001111",
    "pwd": "654321",
}

recharge_params = {
    "mobilephone": "18600001111",
    "amount": 318964,
}

headers = {
    'user-agent': 'Mozilla/5.0 ljs/1.0'
}

# 向服务器发起post请求

# 登录，会产生Set-Cookie数据
login_resp = requests.post(login_url, data=login_params, headers=headers)

# cookies类似于字典，支持字典所有操作
# cookie = login_resp.cookies['JSESSIONID']
a_cookie = login_resp.cookies
# 充值，如果不带cookie会充值失败，会重定向到其他页面，比如会跳转到重新登录，因为每次访问http都是无状态的
recharge_resp = requests.post(recharge_url, data=recharge_params, headers=headers, cookies=a_cookie)
