#Напишите программу, которая принимает на вход координаты 
#двух точек и находит расстояние между ними в 2D пространстве.
#Пример:
#- A (3,6); B (2,1) -> 5,09
#- A (7,-5); B (1,-1) -> 7,21
import math
print('Введите координаты первой точки: ')
number_x_1 = int(input())
number_y_1 = int(input())
print('Введите координаты второй точки: ')
number_x_2 = int(input())
number_y_2 = int(input())
result = round(math.sqrt(((number_x_2 - number_x_1)**2) + ((number_y_2 - number_y_1)**2)), 2)
print(f'Расстояние между точками = {result}')
