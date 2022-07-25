#Напишите программу, которая найдёт произведение пар чисел списка.
#Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#Пример:
#- [2, 3, 4, 5, 6] => [12, 15, 16];
#- [2, 3, 5, 6] => [12, 15]

def create_mass(numbers:int):
    my_list = []
    for index in range(numbers):
        my_list.append(int(input('элемент: ')))
    return my_list

def multiplication_frs_and_scn(mass:list):
    n = 0
    result = []
    if len(mass)%2 == 0:
        n = len(mass)//2
    else:
        n = len(mass)//2+1
    for i in range(n):
        result.append(mass[i] * mass[(len(mass))- 1 - i])
    return result


number = create_mass(int(input('Введём колличество элемента массива:')))
print(number)
 
result = multiplication_frs_and_scn(number)
print(result)

    


