#Напишите программу, которая принимает на вход координаты точки (X и Y),
#причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
#в которой находится эта точка (или на какой оси она находится).
#Пример:
#- x=34; y=-30 -> 4
#- x=2; y=4-> 1
#- x=-34; y=-30 -> 3

x = int(input('Введите значение координаты X: '))
y = int(input('Введите значение координаты Y: '))
if (x > 0 and y > 0) and (x != 0 and y != 0): #четверть 1
    print('Заданная точка находится в четверти № 1.')
elif (x < 0 and y > 0) and (x != 0 and y != 0): #четверть 2
    print('Заданная точка находится в четверти № 2.')
elif (x < 0 and y < 0) and (x != 0 and y != 0): #четверть 3
    print('Заданная точка находится в четверти № 3.')
elif (x > 0 and y < 0) and (x != 0 and y != 0): #четверть 4
    print('Заданная точка находится в четверти № 4.')
else:
    print('Данные введены некорректно!')