#Реализуйте алгоритм перемешивания списка.

from random import randint

def create_list(size_list: int):
    list = []
    list = [0] * size_list
    print(list)

def fill_list(list: list, max: int, min: int, size_list: int ):
    list=[randint(min,max) for i in range(size_list)]
    print(list)

size_list = int(input('Введите размер массива: '))
print('Введите максимальное и минимальное значение для массива: ')
max = int(input('max = '))
min = int(input('min = '))

list = create_list(size_list)
fill_list(list, max, min, size_list)