# Вычислить число c заданной точностью d
# Пример:
# при $d = 0.001, π = 3.141

d = 0.001


def given_precision(precision: float) -> float:
    from cmath import pi
    pi_number = str(pi)
    res = ""
    for i in range(len(str(precision))):
        res += pi_number[i]
    return float(res)


print(given_precision(d))
