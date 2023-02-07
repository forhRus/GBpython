from telebot import *
from config import TOKEN
import datetime

bot = TeleBot(TOKEN)
choice = 0

@bot.message_handler(commands=['start'])
def start(msg: types.Message):
    mrk = types.ReplyKeyboardMarkup(resize_keyboard=True)
    key1 = types.KeyboardButton("Рациональные")
    key2 = types.KeyboardButton("Комплексные")
    mrk.add(key1, key2)
    bot.send_message(msg.chat.id, f'Калькулятор\nСделайте выбор с какими числами работать', reply_markup=mrk)

@bot.message_handler(content_types=['text'])
def set_choice(msg):
    global choice
    remove = types.ReplyKeyboardRemove()
    if msg.text == 'Рациональные':
        bot.send_message(msg.chat.id, 'Выбран режим работы с рациональным числами', reply_markup=remove)
        choice = 1
    elif msg.text == 'Комплексные':
        bot.send_message(msg.chat.id, 'Выбран режим работы с действительными числами', reply_markup=remove)
        choice = 0
    bot.send_message(msg.chat.id, "Введите выражение")
    bot.register_next_step_handler(msg, controller)

def controller(msg):
    line = parse(msg.text)
    solution(msg, line)
    loging(msg)
    try_again(msg)

def parse(text):
    exp = text.replace('+', ' + ').replace('-', ' - ').replace('*', ' * ')\
        .replace('/', ' / ').replace('(',' ( ').replace(')', ' ) ').split()
    new_exp = [exp[0]]
    for i in range(1, len(exp)):
        if exp[i] + exp[i - 1] == '//':
            new_exp[-1] = '//'
        else:
            new_exp.append(exp[i])
    if exp[0] == '-':
        exp[1] = '-' + exp[1]
        exp.pop(0)
    return new_exp

def solution(msg, line: list):
    znak = line[1]
    res = 0
    operation = {'+': lambda x, y: x + y,
                 '-': lambda x, y: x - y,
                 '*': lambda x, y: x * y,
                 '/': lambda x, y: x / y,
                 '//': lambda x, y: x // y,
                 '%': lambda x, y: x % y}
    if choice:
        a, b = int(line[0]), int(line[2])
        for c in operation:
            if znak == c:
                res = operation[c](a, b)
                bot.send_message(msg.chat.id, res)
    else:
        if znak in ('//', '%'):
            bot.send_message(msg.chat.id, "с рациональными числами не возможна такая операция")
        else:
            a, b = complex(line[0]), complex(line[2])
            for c in operation:
                if znak == c:
                    res = operation[c](a, b)
                    bot.send_message(msg.chat.id, res)

def try_again(msg):
    if msg.text in ('Повторить', '/start'):
        start(msg)
    else:
        mrk = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key1 = types.KeyboardButton("Повторить")
        mrk.add(key1)
        bot.send_message(msg.chat.id, 'Хотите ввести ещё одно выражение?', reply_markup=mrk)
        bot.register_next_step_handler(msg, try_again)

def loging(msg: types.Message):
    path = 'log.txt'
    with open(path, 'a', encoding='utf8') as date:
        f = date
        f.write(f'{msg.from_user.id};{msg.from_user.first_name};{msg.text};{datetime.datetime.now().time()}\n')


bot.infinity_polling()