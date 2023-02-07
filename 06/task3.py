# Реализуйте алгоритм перемешивания списка. 
# НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, 
# максимум использование библиотеки Random для получения случайного int
import random

# number = int(input('Введите целое число: '))
# my_list = []
# for i in range(number):
#     my_list.append(i)
my_list = [i for i in range(1, int(input('Введите целое число: ')) + 1)]
print(*my_list, sep = ', ')

# for i in range(len(my_list)):
#     my_list.insert(i, my_list.pop(random.randint(0, len(my_list)-1)))
[my_list.insert(i, my_list.pop(random.randint(0, len(my_list)-1))) for i in range(len(my_list))]
# random.shuffle(my_list)
print(*my_list, sep = ', ')