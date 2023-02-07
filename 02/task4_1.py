# Реализуйте алгоритм перемешивания списка. 
# НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, 
# максимум использование библиотеки Random для получения случайного int
import random

number = int(input('Введите целое число: '))
my_list = []

for i in range(number):
    my_list.append(i)

print(*my_list, sep = ', ')

for i in range(number):
    my_list.insert(i, my_list.pop(random.randint(0, number-1)))

print(*my_list, sep = ', ')