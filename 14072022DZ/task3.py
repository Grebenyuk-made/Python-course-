#Задайте список из вещественных чисел. Напишите программу, 
#которая найдёт разницу между максимальным и минимальным значением дробной части элементов
#Пример:
#- [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def create_mass(numbers:int):
    my_list = []
    for index in range(numbers):
        my_list.append(float(input('элемент: ')))
    return my_list

def findfloat_max(my_list):
    my_max = float(my_list[0])
    for i in range(len(my_list)):
        if float(my_list[i]) > my_max : my_max = float(my_list[i])
    print(f'max = {my_max}')
    return my_max

def findfloat_min(my_list):
    my_min = float(my_list[0])
    for i in range(len(my_list)):
        if float(my_list[i]) < my_min : my_min = float(my_list[i])
    print(f'min = {my_min}')
    return my_min
    
number = create_mass(int(input('Введём колличество элемента массива:')))
print(number)

result = round(findfloat_max(number) - findfloat_min(number), 3)
print(f'Разница максимального и минимального = {result}.')

#решение с использованием max и min

#maxx = max(number)
#minn = min(number)
#result = maxx - minn
#print(result)

