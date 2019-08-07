import re

# target_str = '{"mobilephone": "${not_existed_tel}", "pwd": "123456", "regname": "KeYou"}'


# 1、将正则字符串编译成Pattern模式对象
mobile_pattern = re.compile(r"\$\{not_existed_tel\}")
regname_pattern = re.compile(r"\$\{regname\}")

# 2、使用Pattern对象去匹配文本
# match 从头匹配，如果未匹配上，则返回None，如果能匹配则返回match对象
# match_obj = re.match(pattern, target_str)

# search 从目标字符串target_str查找模式对象pattern，如果未匹配上，则返回None，如果能匹配则返回match对象
# match_obj = re.search(pattern, target_str)

# sub 从目标字符串target_str查找模式对象pattern，如果找到，则把中间参数“13711223344”替换模式对象pattern
# re.sub(pattern, "13711223344", target_str)


def not_existed_tel_replace(data):
    if re.search(mobile_pattern, data):
        data = re.sub(mobile_pattern, "13711223344", data)

    if re.search(regname_pattern, data):
        data = re.sub(regname_pattern, "KeYou", data)

    return data


if __name__ == '__main__':
    target_str1 = '{"mobilephone": "${not_existed_tel}", "pwd": "123456", "regname": "KeYou"}'
    target_str2 = '{"mobilephone": "${not_existed_tel}", "pwd": "123456", "regname": "${regname}"}'
    target_str3 = '{"mobilephone": "", "pwd": "123456"}'
    target_str4 = '{"mobilephone": "13711223344", "pwd": "123456"}'
    print(not_existed_tel_replace(target_str1))
    print(not_existed_tel_replace(target_str2))
    print(not_existed_tel_replace(target_str3))
    print(not_existed_tel_replace(target_str4))
