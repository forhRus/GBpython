# Задайте список из N элементов, заполненных числами 
# из промежутка [-N, N]. Найдите произведение элементов 
# на указанных позициях. Позиции хранятся в файле file.txt 
# в одной строке одно число.

lenght = int(input('Задайте длинну списка: '))
# my_list = []
multi_number = 1
path = r'C:\Users\Пользовательская\Desktop\repo\python_gb\file.txt'
# for i in range(-lenght, lenght+1):
#     my_list.append(i)
my_list = [i for i in range(-lenght, lenght + 1)]
print(*my_list, sep = ', ')

with open(path, 'r') as data:
    l = list(map(int, data.read().split()))
    for i in l:
        if i < len(my_list):
            multi_number *= my_list[i]

print(multi_number) 
#в файле 1 4 7 
# при длине 5, ответ 8