# Задайте список из n чисел последовательности (1 + 1/n)**n, 
# выведеите его на экран, а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06

number = int(input('Введите число: '))
my_list = []
sum_of_elements = 0

for i in range(1, number+1):
    my_list.append(round((1+1/i)**i, 2))
    
for i in range(len(my_list)):
    sum_of_elements += my_list[i]

print(*my_list, sep = ', ')
print(sum_of_elements)
