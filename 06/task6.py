# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

import random

#генерирую список с величинами от 1 до 6 и длинной от 4 до 8, невкл
my_list = [random.randint(1, 6) for i in range(random.randint(4, 8))]
# multi_list = []
print(my_list)

#считаю произведения пар чисел и добавляю их в новый список
# for i in range(len(my_list) // 2):
#     multi_list.append(my_list[i] * my_list[len(my_list) - 1 - i])
# #если элементов в списке не четное количество, то
# if len(my_list) % 2 != 0:
#     #добавляю в список с произведениями непарный элемент в квадрате
#     #индекс которого - (длина списка - 1) уменьшенная на количество пар
#     multi_list.append(my_list[((len(my_list) -1) - (len(my_list) // 2))] ** 2)
if len(my_list) % 2:
    multi_list = [my_list[i] * my_list[len(my_list) - 1 - i] for i in range(len(my_list) // 2 + 1)]
else:
    multi_list = [my_list[i] * my_list[len(my_list) - 1 - i] for i in range(len(my_list) // 2)]
print(multi_list)

