def del_words(input_str: str):
    my_str_list = input_str.split()
    result = ''
    for word in my_str_list:
        if 'abc' not in word:
            result = ' '.join([result, word])
    result = result[1:]
    return result

my_str = 'dsd abcs fabcdd ablc aa ddsdasdasd'

print(del_words(my_str))