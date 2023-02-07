# Задайте список из N элементов, заполненных числами 
# из промежутка [-N, N]. Найдите произведение элементов 
# на указанных позициях. Позиции хранятся в файле file.txt 
# в одной строке одно число.

lenght_list = int(input('Задайте длинну списка: '))
my_list = []
multi_number = 1
path = 'file.txt'

for i in range(-lenght_list, lenght_list+1):
    my_list.append(i)

print(*my_list, sep = ', ')

with open(path, 'r') as data:
    for l in data:
        if int(l) < len(my_list):
            multi_number *= my_list[int(l)]
data.close()

print(multi_number) 
#в файле 1 4 7 
# при длине 5, ответ 8