# 将年龄大于24的得分更新为99

list1 = [{'userid': 5, 'age': 24, 'score': 97},
         {'userid': 6, 'age': 26, 'score': 82},
         {'userid': 7, 'age': 22, 'score': 90}]

# list1[1]['score'] = 99
# print(list1)

for i in list1:
    if i['age'] > 24:
        i['score'] = 99

print(list1)
