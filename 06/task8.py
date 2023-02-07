# Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.

n = int(input('Задайте число: '))

# for i in range(1, n+1):
#     if n % i == 0:
#         my_list.append(i)
print(f'Простые множители числа {n}:', end=' ')
my_list1 = [i for i in range(1, n + 1) if not n % i]
print(*my_list1, sep=', ')

print(f'Через filter:', end=' ')
my_list = [i for i in range(1, n + 1)]
my_filter_list = list(filter(lambda x: not len(my_list) % x, my_list))
print(*my_filter_list, sep=', ')


