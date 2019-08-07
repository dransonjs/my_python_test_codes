from selenium.webdriver.common.by import By


class LoginLocator:
    phone_locator = (By.XPATH, "//input[@name='phone']")
    pwd_locator = (By.XPATH, "//input[@name='password']")
    login_button_locator = (By.XPATH, "//button[text()='登录']")
    login_error1_locator = (By.XPATH, "//div[@class='layui-layer-content']")
    login_error2_locator = (By.XPATH, "//div[@class='form-error-info']")


class HomeLocator:
    bid_button_locator = (By.XPATH, "//a[@href='/loan/loan_detail/Id/15594.html' and @class='btn btn-special']")
    # bid_button_locator = (By.CLASS_NAME, "btn-special")


class BidLocator:
    bid_input_locator = (By.XPATH, "//input[@class='form-control invest-unit-investinput']")
    # bid_input_locator = (By.CLASS_NAME, "invest-unit-investinput")
    bid_button2_locator = (By.CLASS_NAME, "height_style")
    bid_fail_tip = (By.XPATH, "//div[@class='text-center']")
    tip_button = (By.XPATH, "//a[@class='layui-layer-btn0']")
    bid_success_tip = (By.XPATH, "//div[@class='capital_ts']/following::div[@class='capital_font1 note']")
    look_and_active = (By.XPATH, "//div[@class='capital_btn']/following::button[text()='查看并激活']")


class UserLocator:
    amount_balance = (By.XPATH, "//li[@class='color_sub']")
    invest_project = (By.XPATH, "//div[@data-type='tz']")
    bid = (By.XPATH, "//a[@href='/loan/loan_detail/Id/15594.html']")


