#Применение новых методов к старым задачам.
#Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
import math
text1 = ['привет', 'пока' ,'абв', 'самолёт', 'работа' ,'абв', 'сон' , 'обучение' ,'абв', 'путишествие' ]
result1 = list(filter(lambda x = "абв": x != "абв", text1))
print(result1)

#Напишите программу, которая принимает на вход координаты 
#двух точек и находит расстояние между ними в 2D пространстве
def calс (pr , a , b, c, d):
    print(pr (a  , b, c, d))
coor1 = 10
coor2 = 20
coor3 = 30
coor4 = 40
mult = lambda a,b,c,d: round(math.sqrt((a - b)**2) +((c - d)**2))
calс(mult, coor1,coor2,coor3,coor4)

#Напишите программу, которая принимает на вход вещественное 
#число и показывает сумму его цифр. 
def finding_sum (numbers: float) -> int:
    result = 0
    numbers_str = str(numbers)
    for i in numbers_str:
        if i != '0' and '.':
            result += int(i)
    print(result)

numbers = float(input('Введите вещественное число: '))
result2 = list(map(finding_sum, numbers))
print(result2)