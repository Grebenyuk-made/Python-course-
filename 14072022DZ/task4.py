#Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#Пример:
#- 45 -> 101101 #- 3 -> 11 #- 2 -> 10

def find_binary(number):
    my_str = '' 
    while number > 0:
        my_str = str(number% 2) + my_str
        number = number // 2
    return my_str


number = int(input('Введите число: '))
result = find_binary(number)
print(f'Переводим данное число {number} в двоичное число = {result}')
