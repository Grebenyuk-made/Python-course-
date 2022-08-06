#Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
def create_strmass(numbers:int):
    my_list = []
    for index in range(numbers):
        my_list.append(str(input('элемент: ')))
    return my_list

def text_filtering (text:list , word:str):
    result = [i for i in text if word not in i ]
    print(result)

choice1 = int(input('Ввыберите вариант 1.Использовать заготовленый массив слов. 2.Использовать свой. '))
choice2 = int(input('Ввыберите вариант 1.Использовать заготовленое слово. 2.Использовать своё. '))
if choice1 == 1 and choice2 == 1:
    text = ['привет', 'пока' ,'абв', 'самолёт', 'работа' ,'абв', 'сон' , 'обучение' ,'абв', 'путишествие' ]
    word = 'абв' 
    print(f'Массив слов - {text}. \nСлово которое исключаем - {word}.\n')
    print(f'Результат - {text_filtering(text ,word)}.')
elif choice1 == 2 and choice2 == 2:
    number = create_strmass(int(input('Введём колличество элемента массива:')))
    find_word = str(input('Какое слово будем исключать: '))
    print(f'Результат - {text_filtering(number, find_word)}.')



