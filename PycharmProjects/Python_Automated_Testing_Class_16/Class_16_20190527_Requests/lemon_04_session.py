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
# 返回一个Session对象，在整个会话过程中会自动记录cookie
a_session = requests.Session()

# 登录
login_resp = a_session.post(login_url, data=login_params)

# 充值
recharge_resp = a_session.post(recharge_url, data=recharge_params)
