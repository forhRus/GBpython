# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит заданное количество конфет. 
# Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход 
# можно забрать не более чем 28 конфет. Все 
# конфеты оппонента достаются сделавшему последний ход.
# a) Добавьте игру против бота
# b) Подумайте как наделить бота 'интеллектом'

from random import *

count = randint(50, 100)
turn = randint(0, 1)

def player_turn():
    while True:
        turn = int(input())
        if 0 < turn < 29:
            return turn
            break
        else:
            print('Вы должны взять минимум 1 и максимум 28 конфет. Играйте честно.')
    
while count > 0:
    print(f'Количество конфет: {count}')
    if turn:
        print('Ваш ход: ', end = '')
        count -= player_turn()
        turn = 0
    else:
        if count % 29 > 0:
            bot_turn = int(round(count % 29, 2))
        else:
            bot_turn = randint(1, 28)
        print(f'Бот захапал {bot_turn}')
        count -= bot_turn
        turn = 1
else:
    if turn == 1:
        print('Победил Бот')
    else:
        print('Вы победили')

           
    



