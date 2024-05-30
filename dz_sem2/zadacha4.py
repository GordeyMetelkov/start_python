# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
import random
number = int(input("Введите количество элементов N: "))
list = [random.randint(-number, number) for _ in range(number)]
print(list)
compos = 1
positions = input("Введите через пробел номера позиций для произведения: ")
for k in range(len(positions.split())):
    compos *= list[int(positions.split()[k]) - 1]
print(f"Результат: {compos}")
