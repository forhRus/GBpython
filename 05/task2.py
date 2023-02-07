# Создайте программу для игры в 'Крестики-нолики'
# НЕОБЯЗАТЕЛЬНО Добавить игру против бота с интеллектом
from random import *

# игрок может выбрать поле от 1 до 9, повтор не допускается.
def val_player_turn(l:list):
    while True:
        turn = int(input())
        if 0 < turn < 10 and not l[turn-1].isalpha():
            return turn
        elif 0 < turn < 10 and l[turn-1].isalpha():
            print('Эта клетка уже помечена')
        else:
            print('Введите значение от 1 до 9')

# функция принимает t - чей ход, l - список игрового поля, l_bot - оставшиеся варианты для choise бота
def lap(t: int, l: list, l_bot: list):
    if t:
        print('Ваш ход: ', end = '')
        x = val_player_turn(l)  
        l[x-1] = 'X'  #  вносим изменения на поле
    else:
        x = choice(l_bot) 
        print('Бот выбрал', x) 
        l[x-1] = 'O'  
    l_bot.remove(x)  #  удаляем вариант для бота
    t = (t + 1) % 2  #  меняем очередь
    return t, l, l_bot

# проверка на выиграшную комбинацию
def is_winer(l: list):
    var = ('XXX', 'OOO')
    win = (l[0]+l[1]+l[2], l[3]+l[4]+l[5], l[6]+l[7]+l[8], l[0]+l[4]+l[8], l[6]+l[4]+l[2], l[0]+l[3]+l[6], l[1]+l[4]+l[7], l[2]+l[5]+l[8])
    for i in var:
        if i in win:
            return True
        else:
            return False  

tale = ['1', '2', '3', '4', '5', '6', '7', '8', '9']  #  игровое поле
l_bot_choise = [i for i in range(1, 10)]  #  варианты выбор для бота
turn = randint(0, 1)  #  первый ход, а потом флаг
print(f'{tale[0:3]}\n{tale[3:6]}\n{tale[6:9]}')  

for i in range(10):
    turn, tale, l_bot_choise = lap(turn, tale, l_bot_choise)
    print(f'{tale[0:3]}\n{tale[3:6]}\n{tale[6:9]}')  #  выводим игровое поле после каждого хода
    if is_winer(tale):  #  прекращаем играть, если кто-то победил
        if turn == 1:
            print('Победил Бот')
        else:
            print('Вы победили')

        break
else:
    print('Ничья')
    

