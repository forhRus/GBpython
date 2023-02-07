# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на позиции с нечетным индексом.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random

my_list = [random.randint(0, 10) for i in range(random.randint(4, 8))]
sum = 0

print(my_list)

for i in range(1, len(my_list), 2):
    sum += my_list[i]

print(sum)
