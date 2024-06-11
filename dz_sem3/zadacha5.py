# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
def fibonaci(i):
    if i in (1, 2):
        return 1
    elif i == 0:
        return 0
    return (fibonaci(i - 1) + fibonaci(i - 2))


n = 8
fib_list = []
for j in range(1, n + 1):
    fib_list.append(fibonaci(j))
    fib_list.insert(0, fibonaci(j))
fib_list.insert(j, 0)
for j in range(n):
    if j % 2 == 0:
        fib_list[j] *= -1
print(fib_list)
