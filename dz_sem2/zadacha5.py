# Реализуйте алгоритм перемешивания списка.
from random import randint
list = [1, 2, 3, 4, 5, 6, 7]
for i in range(len(list)):
    k = randint(0, len(list)-1)
    temp = list[i]
    list[i] = list[k]
    list[k] = temp
print(list)