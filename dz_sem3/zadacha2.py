# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];

def fill_list(base_list):
    from random import randint
    len_value = randint(5, 10)
    for i in range(len_value):
        base_list.append(randint(-5, 5))
    return base_list


def compos_pos(base_list):
    new_list = []
    middle_pos = len(base_list) // 2
    if len(base_list) % 2 == 1:
        middle_pos += 1
    for i in range(len(base_list)):
        if i < middle_pos:
            new_list.append(base_list[i] * base_list[-i - 1])
            i += 1
    return new_list
if __name__ == '__main__':
    my_list = []
    fill_list(my_list)
    print(my_list, "->", compos_pos(my_list))
