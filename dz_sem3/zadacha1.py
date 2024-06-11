# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.

def fill_list(base_list):
    from random import randint
    len_value = randint(5, 10)
    for i in range(len_value):
        base_list.append(randint(-5, 5))
    return base_list


def sum_pos(base_list):
    my_sum = 0
    for i in range(1, len(base_list), 2):
        my_sum += base_list[i]
    return my_sum


my_list = []
print(fill_list(my_list))
print(sum_pos(my_list))
