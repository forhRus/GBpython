# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

def ValidateQuarter (x):
    if 0 < x < 5:
        return True
    print('Некорректный ввод!')
    return False

def GetCoord (q):
    if q == 1:
        print('x > 0 and y > 0')
    elif q == 2:
        print('x < 0 and y > 0')
    elif q == 3:
        print('x < 0 and y < 0')
    else:
        print('x > 0 and y < 0')

quarter = int(input('Введите четверть: '))
1
if(ValidateQuarter(quarter)):
    GetCoord(quarter)
    