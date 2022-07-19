#Напишите программу, которая принимает на вход вещественное 
#число и показывает сумму его цифр. 
#Пример: - 6782 -> 23 
# - 0,56 -> 11

def finding_sum (numbers: float) -> int:
    result = 0
    numbers_str = str(numbers)
    for i in numbers_str:
        if i != '0' and '.':
            result += int(i)
    print(result)

numbers = int(input('Введите вещественное число: '))
print('Результат равен - ')
finding_sum(numbers)
