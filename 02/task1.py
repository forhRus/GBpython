# Напишите программу, которая принимает 
# на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

number = float(input('Введите число: '))
print(number)

my_list = str(number).split('.')
number = my_list[0] + my_list[1]

sum_of_digit = 0  
for i in range(len(number)):
    sum_of_digit += int(number[i])

print(sum_of_digit)

