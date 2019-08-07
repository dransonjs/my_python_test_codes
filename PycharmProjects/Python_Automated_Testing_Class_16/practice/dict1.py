# 测试题目解析
# 1.拼接一个HTTP请求；
# 2.从接口返回的JSON文件中获取对应的值；
# 3.两个接口（或者一个接口与数据库）返回的值进行对比校验，或判断相同，或判断不同；

import json
# 请用代码实现下面json格式的拼接
dict1 = {
    "plats": [1],
    "content": "test数据",
    "target": 1,
    "type": 1,
    "registrationIds": ["5d3180df76f8d1e305cf8457","5jdajog3232djajgal9bc08y"],
    "offlineTime": 1
}

json_data = json.dumps(dict1)
print(json_data)

# 请用代码实现，将categoryList和valueList的值以键值对的方式，存入hashmap中
dict2 = {
    "valueList": [7751, 7780, 7737, 7626, 7677, 7716, 6632],
    "categoryList": [
        "2019-07-16 00:00:00",
        "2019-07-17 00:00:00",
        "2019-07-18 00:00:00",
        "2019-07-19 00:00:00",
        "2019-07-20 00:00:00",
        "2019-07-21 00:00:00",
        "2019-07-22 00:00:00"
    ]
}

value_list = dict2["valueList"]
category_list = dict2["categoryList"]
hash_map = dict(zip(value_list, category_list))
print(hash_map)

tuple1 = ("a", "b", "c")
dict3 = dict.fromkeys(tuple1, 10)
print(dict3)

