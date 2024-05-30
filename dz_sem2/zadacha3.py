# Задайте список из k чисел последовательности (1 + 1\k)^k и
# выведите на экран их сумму.

number = int(input("Введите число k: "))
list = []
sum = 0
for i in range(1,number + 1):
    list.append(round((1+1/i)**i, 2))
    sum+=list[-1]
print(list)
print(sum)