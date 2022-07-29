#Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.

def find_simple_numbers(numbers:int):
    my_list = []
    for i in range(numbers):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            my_list.append(i)
    print(my_list)
    
numbers = int(input('Введите число из которого будут отображены простые числа: '))
find_simple_numbers(f'Список простых чисел {numbers}')
