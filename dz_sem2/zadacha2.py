# Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

number = int(input("Введите число N: "))
res_list = []
compos = 1
i = 1
while i <= number:
    compos *= i
    res_list.append(compos)
    i += 1
print(res_list)