#Задайте список из N элементов, заполненных числами из промежутка [-N, N].
#Найдите произведение элементов на указанных позициях. 
#Позиции хранятся в файле file.txt в одной строке одно число
import random 
def create_list(number: int) -> list:
    list = []
    for i in range(0, number):
        list.append(random.randint(-number, number +1))
    print(list)

def find_sum (list, number_1, number_2):
    sum = 0
    for i in range(list):
        if i == number_1:
            number_1 = i
    print(number_1)

    for i in range(list):
        if i == number_2:
            number_2 = i
    print(number_2)
    sum = number_1 * number_2 
    print(sum)

list = int(input('Введите число N: '))
create_list(list)
print(list)
number_1 = int(input('Введите число из списка: '))
number_2 = int(input('Введите число из списка: '))
print(find_sum(list, number_1, number_2))

        
