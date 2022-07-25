#1.Задайте список из нескольких чисел. Напишите программу,
#которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#Пример:
#- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def create_mass(numbers:int):
    my_list = []
    for index in range(numbers):
        my_list.append(int(input('элемент: ')))
    return my_list

def sum_even_numbers(mass:list):
    number = 0
    for index in range(len(mass)):
        if index % 2 == 0:
            number += int(mass[index])
    return number

number = create_mass(int(input('Введём колличество элемента массива:')))
print(f'Изначальный список {number} .')
print('Сумма всех чисел которые находятся на нечётных позициях = ')
print(sum_even_numbers(number))