# Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
import decimal
import math
from decimal import Decimal

xA = int(input("Введите координату точки A по оси Х:"))
yA = int(input("Введите координату точки A по оси Y:"))
xB = int(input("Введите координату точки B по оси Х:"))
yB = int(input("Введите координату точки B по оси Y:"))
distance = float(math.sqrt((xA-xB)**2+(yA-yB)**2))
distance = f'{str(distance).split(".")[0]}.{str(distance).split(".")[1][0:2]}'
print("Расстояние между точками", float(distance))