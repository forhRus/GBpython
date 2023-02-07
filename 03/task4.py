# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

import random

num = random.randint(1, 10)
bi_num = num
bi_numbers_list = []
print('num = ', num)

while bi_num > 0:
    if bi_num == 0:
        break
    bi_numbers_list.append(bi_num % 2)
    bi_num = bi_num // 2

print('деление на 2', bi_numbers_list)
bi_numbers_list.reverse()
print('revers = ', bi_numbers_list)

for i in range(len(bi_numbers_list)):
    bi_num += int(bi_numbers_list[i])
    if i < (len(bi_numbers_list)-1):
        bi_num *= 10

print(num, '-', bi_num)