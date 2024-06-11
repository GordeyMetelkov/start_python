# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
import math


def fill_list(base_list):
    import random
    len_value = random.randint(4, 7)
    for i in range(len_value):
        base_list.append(round(random.uniform(0, 5.5), 2))
    return base_list


def remains_diff(base_list):
    max_remain = base_list[0] % 1 * 100
    min_remain = base_list[0] % 1 * 100
    for i in base_list:
        if i % 1 * 100 < min_remain:
            min_remain = i % 1 * 100
        elif i % 1 * 100 > max_remain:
            max_remain = i % 1 * 100
    return int(max_remain - min_remain) / 100


my_list = []
print(fill_list(my_list))
print(remains_diff(my_list))
# print(remains_diff([1.1, 1.2, 3.1, 5, 10.01]))

