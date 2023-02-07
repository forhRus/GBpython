# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

day = int(input('Введите день недели: '))

week = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']

if 0 < day < 8:
    if 0 < day < 6:
        print(week[day-1])
    else:
        print(f'{week[day-1]}. Ура, выходной!')
    
else:
    print('Некорректное значение')