# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

import random

num = random.randint(5, 10)
# my_list = []

def fib(n):
    if n >= 0:
        if n == 0:
            return 0
        elif n in [1, 2]:
            return 1
        else:
            return fib(n - 1) + fib(n - 2)
    else:
        return fib(n + 2) - fib(n + 1)

# for i in range(-num, num + 1):
#     my_list.append(fib(i))
my_list = [fib(i) for i in range(-num, num+1)]

print(num)
print(my_list)