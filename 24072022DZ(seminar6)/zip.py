#Примеры применения и использования Zip.

boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
girls.sort()
boys.sort()
dating = zip(boys, girls)
for company in dating:
  print(f"{company[0]} и {company[1]}")