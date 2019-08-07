from suds.client import Client
from script.mysql_class import HandleMysql

send_m_code_url = "http://120.24.235.105:9010/sms-service-war-1.0/ws/smsFacade.ws?wsdl"
send_m_code_client = Client(send_m_code_url)
# print(send_m_code_client)
send_m_code_params = {"client_ip": None, "mobile": "13711223344", "tmpl_id": "1"}
result1 = send_m_code_client.service.sendMCode(send_m_code_params)
print(result1)

# url = "http://120.24.235.105:9010/finance-user_info-war-1.0/ws/financeUserInfoFacade.ws?wsdl"
# client = Client(url)
# print(client)
#
# do_mysql = HandleMysql()
# sql = "SELECT Fverify_code FROM `t_mvcode_info_3` WHERE Fmobile_no=13711223344"
# sql_res = do_mysql.sql_execute(sql)
# verify_code = sql_res["Fverify_code"]
#
# register_params = {"verify_code": verify_code,
#                    "user_id": "dranson",
#                    "channel_id": "2",
#                    "pwd": "222222",
#                    "mobile": "13711223344",
#                    "ip": "182.46.25.1"}
# result2 = client.service.userRegister(register_params)
# print(result2)

# print(client)
# sql2 = "SELECT Fuid FROM `t_user_info` WHERE Fuser_id='dranson'"
# sql_res2 = do_mysql.sql_execute(sql2)
# uid = sql_res2["Fuid"]

# verify_true_name_params = {"uid": uid,
#                            "true_name": "剑圣",
#                            "cre_id": "441521198803188237"}
# result3 = client.service.verifyUserAuth(verify_true_name_params)
# print(result3)

# bind_bank_card_params = {"uid": uid,
#                          "pay_pwd": "789456",
#                          "mobile": "13711223344",
#                          "cre_id": "441521198803188237",
#                          "user_name": "剑圣",
#                          "cardid": "6225881304837593",
#                          "bank_type": 1001,
#                          "bank_name": "招商银行"}
# result4 = client.service.bindBankCard(bind_bank_card_params)
# print(result4)
