def simple_num(num: int):
    if num in (1, 2, 3):
        return True
    else:
        middle = int(num / 2)
        for i in range(2, middle):
            if num % i == 0:
                return False
    return True


def simple_mult(num: int):
    result = []
    i = 2
    while i * i <= num:
        while num % i == 0:
            result.append(i)
            num //= i
        i += 1
    if num > 1:
        result.append(num)
    return result


print(simple_mult(20))