#Задайте последовательность чисел. Напишите программу, 
#которая выведет список неповторяющихся элементов исходной последовательности.

def create_mass(numbers:int):
    my_list = []
    for index in range(numbers):
        my_list.append(int(input('элемент: ')))
    return my_list

def find_non_recurring(number:list):    
    result = []
    for n in number:
        if n not in result:
            result.append(n)
    return result

def find_non_recurringV2(number:list):  
    result = list(set(number))
    return result

def find_only_non_recurring(number:list):  
    result = []
    for i in number:
        count = 0
        for j in number:
            if(i == j ):
                count += 1
        if (count == 1 ):
            result.append(i)
    return result


numbers = create_mass(int(input('Введём колличество элемента массива:')))
result1 = find_non_recurring(numbers)
print(f'Находим неповторяющиеся числа через цикл = {result1}.')
result2 = find_non_recurringV2(numbers)
print(f'Находим неповторяющиеся числа через "set" = {result2}.')
result3 = find_only_non_recurring(numbers)
print(f'Находим только неповторяющиеся числа через цикл = {result3}.')