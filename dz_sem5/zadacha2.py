first = ''
with open('vhod.txt', 'r') as data:
    first = data.read()


def rle(first):
    count = 1
    second = ''
    i = 0
    for i in range(len(first) - 1):
        if first[i] == first[i + 1]:
            count += 1
            if i + 1 == len(first) - 1:
                second += str(count) + first[i]
        else:
            second += str(count) + first[i]
            count = 1
    return second

with open('vyhod.txt', 'w') as file:
    file.write(rle(first))