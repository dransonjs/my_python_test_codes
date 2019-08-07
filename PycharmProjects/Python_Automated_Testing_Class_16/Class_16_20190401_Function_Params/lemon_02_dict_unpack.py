dict_1 = {'name': '柠檬小姐姐', 'age': 18}
a, b = dict_1
print(a, b)

a, b = dict_1.items()
print(a, b)

(a, aa), (b, bb) = dict_1.items()
print(a, aa, b, bb)