# Напишите программу, которая принимает на вход число N 
# и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

number = int(input('Введите число: '))
temp = 1
for i in range(1, number +1):
    temp *= i
    print(temp)

# my_list = [1]

# temp = 1 
# for i in range(1, number + 1):
#     temp *= i
#     my_list.append(temp)
        
# print(*my_list, sep = ', ')