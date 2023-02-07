from telebot import types, TeleBot
from config import TOKEN
from random import *

bot = TeleBot(token=TOKEN)
f_new_game = False
turn = 0
count = 0
candy = {'конфета': [1], 'конфеты': [2, 3, 4], 'конфет': [0, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]}
rules = 'Правила просты\n1. Игрок и бот по очереди берут конфеты из общей кучи.\n' \
            '2. Побеждает тот, кто захапал последнюю конфету. Остальные конфеты также достаются ему.\n' \
            '3. За раз можно брать не больше 28 конфет и не меньше 1.\n' \
            '4. Количество конфет и первый ход рандом. Не надо мне тут заносить конфет. Рандом я сказал.'
menu = 'Меню: \n'\
       '/start - запуск программы\n'\
       '/game - Новая игра\n'\
       '/rules - Правила\n'\
       '/finish - Закончить\n'\
       '/menu - Меню'

@bot.message_handler(commands=['start'])
def process_start_command(message: types.Message):
    global menu
    bot.send_message(message.chat.id, 'Бот хочет бросить вам вызов в игре "захапай конфет".')
    bot.send_message(message.chat.id, menu)

@bot.message_handler(commands=['menu'])
def process_menu_command(message: types.Message):
    bot.send_message(message.chat.id, menu)

@bot.message_handler(commands=['rules', 'правила'])
def process_rules_command(message: types.Message):
    bot.send_message(message.chat.id, rules)

@bot.message_handler(commands=['game'])
def process_game_command(message: types.Message):
    global f_new_game
    global candy
    global count
    global turn
    if f_new_game == True:
        bot.send_message(message.chat.id,'Игра не завершена.\nЕсли хотите завершить её введите команду "/finish"')
    else:
        f_new_game = True
        count = randint(70, 150)
        turn = randint(0, 1)
        bot.send_message(message.chat.id, 'Игра началась.')
        bot.send_message(message.chat.id, 'Удачи.')
        bot.send_message(message.chat.id, f'На столе {count} {val_candy(count, candy)}.')
        play(message)

@bot.message_handler(commands=['finish'])
def process_finish_command(message: types.Message):
    global f_new_game
    if f_new_game:
        f_new_game = False
        bot.send_message(message.chat.id, 'Игра завершена. Если хотите сыграть ещё, введите команду "/game"')
    else:
        bot.send_message(message.chat.id,'Мы ещё даже не начинали играть. Введите команду "/game"')

def play(msg):
    global f_new_game
    if f_new_game:
        if turn:
            bot.send_message(msg.chat.id, 'Ваш ход.')
            bot.register_next_step_handler(msg, player_turn)
        else:
            bot_turn(msg)
    else:
        bot.send_message(msg.chat.id, 'Если хотите начать новую игру, введите команду "/game"')

def player_turn(msg):
    global f_new_game
    global count
    global turn
    if msg.text.isdigit():
        take = int(msg.text)
        if 0 < take < 29:
            count -= take
            turn = 0
            if count < 0:
                count = 0
            bot.send_message(msg.chat.id, f'Осталось {count} {val_candy(count, candy)}.')
            check_count(msg)
        else:
            bot.send_message(msg.chat.id, 'Вы должны взять минимум 1 и максимум 28 конфет. Играйте честно.')
    else:
        bot.send_message(msg.chat.id, 'Введите число.')
    play(msg)

def bot_turn(msg):
    global f_new_game
    global turn
    global count
    global candy
    bot_take = 0
    if count % 29 > 0:
        bot_take = int(round(count % 29, 2))
    else:
        bot_take = randint(1, 28)
    count -= bot_take
    turn = 1
    bot.send_message(msg.chat.id, f'Bot захапал {bot_take} {val_candy(count, candy)}. '
                                  f'Осталось {count} {val_candy(count, candy)}.')
    check_count(msg)
    play(msg)

def check_count(msg):
    global f_new_game
    global count
    global turn
    if f_new_game:
        if count <= 0:
            if turn == 1:
                bot.send_message(msg.chat.id, 'Победил Bot!')
            else:
                bot.send_message(msg.chat.id, 'Вы победили!')
            f_new_game = False

def val_candy(n: int, d: dict):
    x = n % 100
    if not x <= 20:
        x = n % 10
    for k in d:
        if x in d[k]:
            return k

bot.infinity_polling()

