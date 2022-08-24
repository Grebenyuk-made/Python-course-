#Примеры применения и использования Filter.

number_list1 = range(-5, 5)
result1 = list(filter(lambda x: x < 0, number_list1))
print(result1)

number_list2 = range(-20, 5)
result2 = list(filter(lambda x: x > 0, number_list2))
print(result2)

number_list3 = range(-100, 100)
result3 = list(filter(lambda x: x % 2 == 0, number_list3))
print(result3)

