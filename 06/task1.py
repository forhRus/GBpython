# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

def SetCoord (message):
    return [int(input(f'Задайте {i + 1}-ую координату точки {message}: ')) for i in range[2] ]

def FindDistance(ar1, ar2):
    sum = 0
    for i in range(2):
        sum = sum + (ar1[i] - ar2[i]) ** 2
    return sum ** 0.5

pointA = SetCoord('A')
pointB = SetCoord('B')
print(FindDistance(pointA, pointB))