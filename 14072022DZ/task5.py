#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#Пример:
#- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def minus_fibo(number:int) -> int:
    if number == -1:
        return 1
    elif number == -2:
        return -1
    else:
        return minus_fibo(number + 2) - minus_fibo(number + 1)

def plus_fibo(number:int) -> int:
    if (number <= 1):
        return number
    else:
        return plus_fibo(number - 1) + plus_fibo(number - 2)

def list_fibo(number: int) -> list:
    my_list = []
    for i in range(- number, 0):
        my_list.append(minus_fibo(i))
    for i in range(0, number+1):
        my_list.append(plus_fibo(i))
    return my_list

number = int(input('Введите число: '))
result = list_fibo(number)
print(f'Итоговый список чисел Фибоначчи =  {result}')


