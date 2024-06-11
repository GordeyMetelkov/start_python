def unique_elements(input_list: list):
    result_list = []
    for elem in input_list:
        if input_list.count(elem) == 1:
            result_list.append(elem)
    return result_list

my_list = [1, 1, 2, 3, 4, 5, 5]
print(my_list, '->', unique_elements(my_list))