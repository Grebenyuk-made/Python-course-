#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#Пример:
#- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def find_result (numbers:int)-> list:
    list = []
    result = 1
    for i in range(1, numbers+1):
        result *= i
        list.append(result)
    print(result)

numbers = int(input('Введите число: '))
print('Результат равен - ')
find_result(numbers)