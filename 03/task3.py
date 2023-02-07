# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным 
# значением дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

#генерирую список из 10 элементов с дробными числами.
#чисел после запятой от 1 до 3
amount = random.randint(1, 3)
my_list = [round(random.uniform(0, 10), amount) for i in range(10)]

#максимальное и минимальное значение равно первому элементу
max = round(1 / (10*amount), amount)
min = 1
print(my_list)

for i in range(1, len(my_list)):
    #поиск остатка
    temp = my_list[i] % 1
    if temp > 0:
        if temp > max:
            max = temp
        if temp < min:
            min = temp
    
print('max -', round(max, amount))
print('min -', round(min, amount))
print(round(max - min, amount))



