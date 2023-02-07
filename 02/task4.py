# Реализуйте алгоритм перемешивания списка. 
# НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, 
# максимум использование библиотеки Random для получения случайного int
import random

number = int(input('Введите целое число: '))
my_list = []
revers_list = []

for i in range(number):
    my_list.append(i)

print(*my_list, sep = ', ')

for i in range(number):
    temp_element = my_list.pop(random.randint(0, len(my_list)-1))
    revers_list.append(temp_element)

print(*revers_list, sep = ', ')
