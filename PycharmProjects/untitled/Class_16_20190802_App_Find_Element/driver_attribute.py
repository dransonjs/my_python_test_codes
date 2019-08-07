from appium import webdriver

desired_caps = {
    "automationName": "UiAutomator1",
    "platformName": "Android",
    "platformVersion": "5.1",
    "deviceName": "Android Emulator",
    "appPackage": "com.xxzb.fenwoo",
    "appActivity": "com.xxzb.fenwoo.activity.addition.WelcomeActivity",
    "noReset": True
}

# 注意端口号是否正确
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

# driver属性
# driver.current_package  # 当前包名
# driver.current_activity  # 当前活动页地址，相当于web的url
# driver.context  # 上下文，相当于web的窗口切换，句柄
# driver.contexts  # 所有上下文
# driver.page_source  # 源代码
# driver.capabilities  # 标准化
# driver.device_time  # 设备时间
# driver.location  # 手机定位

# driver操作
# driver.quit()  # 退出app
# 实现页面跳转，打个比方：注册需要填写账号密码手机号才能跳到注册成功页，这个方法可以跳过填写信息直接跳到注册成功页
# 第一个参数为包名，第二个参数为当前活动页地址
# driver.start_activity()
# driver.reset()  # 重置应用数据，清缓存，不是重启手机
# driver.background_app()  # 设置app后台运行多少秒，参数为-1则一直在后台运行
# driver.is_app_installed()  # 判断app是否安装，安卓参数为包名，ios参数为bundle_id
# driver.install_app()  # 安装app，参数为app路径
# driver.close_app()  # 关闭app

