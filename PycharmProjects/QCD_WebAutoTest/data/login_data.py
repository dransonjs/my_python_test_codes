login_success_data = {"phone": "18684720553", "pwd": "python"}

login_fail_data = [{"phone": "", "pwd": "", "tip": "请输入手机号"},
                   {"phone": "1", "pwd": "", "tip": "请输入正确的手机号"},
                   {"phone": "13700001111", "pwd": "", "tip": "请输入密码"}]

login_fail_data2 = [{"phone": "18684720550", "pwd": "1", "tip": "此账号没有经过授权，请联系管理员!"},
                    {"phone": "18684720553", "pwd": "1", "tip": "帐号或密码错误!"}]
