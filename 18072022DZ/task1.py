#Вычислить число c заданной точностью d
#Пример: - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
import math
#print (math.pi)

def round_a_number(number:int):
    if number == 1:
        result = round(math.pi,3)
        print(f'Результат {math.pi} >> {result}')
    elif number == 2:
        float_number = float(input('Введите ваше число: '))
        print(round(float_number, 3))
    else:
        print('Сделайте корректный выбор!')
        
number = int(input('Сделайте выбор: 1.Использовать число ПИ. 2.Ввести своё число.'))
round_a_number(number)