#Задана натуральная степень k. Сформировать случайным образом список коэффициентов
#(значения от 0 до 100) многочлена и записать в файл многочлен степени k.
#Пример:
#- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
from pathlib import Path
import random 

def random_numbers(number: int) -> list: 
    list = [] 
    for i in range(0, number): 
        list.append(random.randint(0, 101)) 
    return list

deegre = int(input('deegre = '))
coef_list = random_numbers(deegre+1) 
my_str = str()

for i in range(0,len(coef_list)): 
    new_number = False
    if (deegre > 1) and (coef_list[i] > 1):
        my_str+= str(coef_list[i])+'*x**('+str(deegre)+')'
        new_number = True 
    elif (deegre > 1) and (coef_list[i] == 1):
        my_str+='x**('+str(deegre)+')' 
        new_number = True 
    elif (deegre == 1) and (coef_list[i] > 1):
        my_str+= str(coef_list[i])+'*x' 
        if (coef_list[i+1] != 0): 
            new_number = True
    elif (deegre == 1) and (coef_list[i] == 1):
        my_str+='x' 
        if (coef_list[i+1] != 0): 
            new_number = True 
    elif (deegre == 0) and (coef_list[i] != 0):
        my_str+=str(coef_list[i])+' = 0' 
    elif (deegre == 0) and (coef_list[i] == 0):
        my_str+=' = 0'

    if new_number: 
        my_str+=' + ' 
    deegre-=1

path = Path('18072022DZ' , 'task4.1.txt')
with open (path, 'a') as number:
    number.writelines(my_str)
print(f'\nФайл записан в {path}\n')
   