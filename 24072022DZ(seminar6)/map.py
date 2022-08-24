#Примеры применения и использования Map.

def sorting (number):
    if number % 2 == 0:
        return number

numbers = [1,2,3,4,5,6,7,8,9,10]
result = list(map(sorting, numbers))
print(result)