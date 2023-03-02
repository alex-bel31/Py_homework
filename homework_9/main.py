import telebot
from telebot import types
import random
from random import randint
bot = telebot.TeleBot("5915826663:AAHAY_Pk9v6GDvDAkJFHJlJANp_jol78Stk")

sweets = 221
max_sweet = 28
user_turn = 0
bot_turn = 0
flag = ""

messages = ['Ваш ход брать конфеты', 'Возьмите конфеты',
            'сколько конфет берем?', 'берите еще', 'Ваш ход']

@bot.message_handler(commands=["start"])
def start(message):
    global flag
    
    bot.send_message(message.chat.id, f"Приветствую вас в игре!")
    bot.send_message(message.chat.id,     "В игре участвуют два игрока\n"
                                          "Первый ход определяется жеребьевкой.\n"
                                          "Игроки ходят, совершая ход друг после друга\n"
                                          "Правила игры:\n"
                                          "У нас есть некоторое количество конфет\n"
                                          "За один ход можно забрать не более 28 конфет\n"
                                          "Тот, кому достанется последняя конфета - проиграл\n")
    bot.send_message(message.chat.id, f"Всего в игре {sweets} конфет")

    flag = random.choice(["user", "bot"])
    if flag == "user":
        bot.send_message(message.chat.id,f"Первым ходите вы")
        controller(message)
    else:
        bot.send_message(message.chat.id, f"Первым хожу я")
        controller(message)
        
def controller(message):
    global flag
    if sweets>0:
        if flag == "user":
            bot.send_message(message.chat.id, f"{random.choice(messages)} введите кол-во конфет от 0 до {max_sweet}")
            bot.register_next_step_handler(message,user_input)
        else:
            bot_input(message)
    else:
        flag = "user" if flag == "bot" else "bot"
        bot.send_message(message.chat.id, f"Победил {flag}!")

def bot_input(message):
    global sweets,bot_turn,flag
    if sweets <= max_sweet:
        bot_turn = sweets
    elif sweets % max_sweet == 0:
        bot_turn = max_sweet - 1
    else:
        bot_turn = sweets % max_sweet - 1
        if bot_turn == 0:
            bot_turn = 1
    sweets -= bot_turn
    bot.send_message(message.chat.id, f"я забираю {bot_turn} конфет")
    bot.send_message(message.chat.id, f"осталось {sweets}")
    flag = "user" if flag == "bot" else "bot"
    controller(message)

def user_input(message):
    global flag,user_turn,sweets
    user_turn = int(message.text)
    sweets -= user_turn
    bot.send_message(message.chat.id, f"осталось {sweets}")
    flag = "user" if flag == "bot" else "bot"
    controller(message)

bot.infinity_polling()