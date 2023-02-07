# Задача 32:  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8
a, b = int(input()), int(input())

def power(a, b):
    if b == 0:
        return 1
    elif b % 2 == 2:
        power(a * a, b / 2)
    else:
        return a * power(a, b - 1)
  
print(power(a, b))
