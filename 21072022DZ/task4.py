#Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
from pathlib import Path 
from collections import Counter

def file_to_str1(path: Path) -> list: 
    with open(path, 'r') as file: 
        return file.readline() 

path1 = Path( 'ED' , '21072022DZ' , 'task4start.txt' )
strr1 = file_to_str1(path1)
print(strr1)

# Первый вариант решения 
d = dict()
for k, v in Counter(strr1).items():
    d.setdefault(v, []).append(k)
print(d)
dd = str(d)

# Второе решение нашёл в интернете очень интересное 

c = Counter(strr1)
res_freq = '\n'.join('{} = {}'.format(tup[0] if tup[0] != "\n" else "\\n", tup[1]) for tup in c.most_common())
print(res_freq)

path = Path( 'ED' , '21072022DZ' , 'task4finish.txt' ) 
with open(path, 'w') as poly: 
    poly.writelines(f'{dd}\n')
    poly.writelines(f'{res_freq}\n')


