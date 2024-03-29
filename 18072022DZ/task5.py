#Даны два файла, в каждом из которых находится запись многочлена.
#Задача - сформировать файл, содержащий сумму многочленов.

from pathlib import Path 
  
  
def file_to_str(path: Path) -> str: 
    with open(path, 'r') as file: 
        return file.readline() 
  
  
def coef_of_str(poly: list) -> list: 
    coefficients = [] 
    for i in poly: 
        if ('x' in i) and ('(' in i): 
            coefficients.append( 
                 [int(i[i.find('(')+1:i.find(')')]), int(i[0:i.find('*')])]) 
        elif ('x' in i) and ('(' not in i): 
             coefficients.append([1, int(i[0:i.find('*')])]) 
        elif ('x' not in i) and (i != '+') and (i != '=') and (i != '0'): 
            coefficients.append([0, int(i)]) 
    return coefficients 
  
  
path1 = Path('18072022DZ', 'task5_1.txt') 
path2 = Path('18072022DZ', 'task5_2.txt') 
str1 = file_to_str(path1) 
str2 = file_to_str(path2) 
split_str1 = str1.split() 
split_str2 = str2.split() 
coef_list1 = coef_of_str(split_str1) 
coef_list2 = coef_of_str(split_str2) 
  
sum_str = str() 
  
for i in coef_list1: 
  
    for j in coef_list2: 
        if (j[0] == i[0] > 1): 
             sum_str += f'{i[1]+j[1]}*x**({i[0]}) + ' 
        elif (j[0] == i[0] == 1): 
            sum_str += f'{i[1]+j[1]}*x + ' 
        elif (j[0] == i[0] == 0): 
            sum_str += f'{i[1]+j[1]} + ' 
  
sum_str = sum_str[0:len(sum_str)-2]+'= 0' 
  
path = Path("18072022DZ", "task5_result.txt") 
with open(path, 'w') as poly: 
    poly.writelines(f'{sum_str}\n') 
print(f'\nФайл записан в {path}\n')
