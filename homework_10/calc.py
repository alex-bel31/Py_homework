import telebot
from telebot import types
import modul
import datetime

bot = telebot.TeleBot("")

@bot.message_handler(commands = ['start'])
def start(message):
    dtn = datetime.datetime.now()
    botlogfile = open('BD.log', 'a')
    print(dtn.strftime("%d-%m-%Y %H:%M"), 'Пользователь ' + message.from_user.first_name, message.from_user.id, 'написал следующее: ' + message.text, file=botlogfile)
    botlogfile.close()
    
    user_name = message.from_user.username
    bot.send_message(message.chat.id,  f"Привет {user_name}, я бот - калькулятор.\n"
                                        "Математические операции для целый чисел: (+,-,/,//,%).\n"
                                        "Если числа комплексные - (+,-,,/).\n")
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    but1 = types.KeyboardButton("Рациональные")
    but2 = types.KeyboardButton("Комплексные")
    markup.add(but1)
    markup.add(but2)
    bot.send_message(message.chat.id, 'Выберите с какими числами хотите работать.', reply_markup=markup)

@bot.message_handler(content_types = ["text"])
def controller(message):
    
    global type_nums
    a = types.ReplyKeyboardRemove()

    if message.text == "Рациональные":
        bot.send_message(message.chat.id, 'Рациональные числа.',reply_markup=a )
        bot.send_message(message.chat.id, 'Введите выражение разделяя каждый знак пробелом.')
        bot.register_next_step_handler(message, controller )
        type_nums = 0

    elif message.text == "Комплексные":
        bot.send_message(message.chat.id, 'Комплексные числа.',reply_markup=a )
        bot.send_message(message.chat.id, 'Введите выражение разделяя каждый знак пробелом.')
        bot.register_next_step_handler(message, controller )
        type_nums = 1
    dtn = datetime.datetime.now()
    botlogfile = open('BD.log', 'a')
    print(dtn.strftime("%d-%m-%Y %H:%M"), 'Пользователь ' + message.from_user.first_name, message.from_user.id, 'написал следующее: ' + message.text, file=botlogfile)
    botlogfile.close()
 
def controller(message):
    line = message.text.split()
    action = line[1]
    if type_nums == 0:      
        x = int(line[0])
        y = int(line[2])
    else: 
        x = complex(line[0])
        y = complex(line[2])
    if action == '+':
        res = modul.sum(x, y)
    elif action == '-':
        res = modul.sub(x, y)
    elif action == '*':
        res = modul.mul(x, y)
    elif action == '/':
        res = modul.div(x, y)
    elif type_nums == 1 and (action == "//" or action == "%"):
        bot.send_message(message.chat.id, "Неверный формат ввода.")
        bot.register_next_step_handler(message, controller)
        start(message)
        return
    elif action == '%':
        res = modul.mod(x, y)
    elif action == '//':
        res = modul.mod1(x, y)
    bot.send_message(message.chat.id,f"Ответ: {res}")
    dtn = datetime.datetime.now()
    botlogfile = open('BD.log', 'a')
    print(dtn.strftime("%d-%m-%Y %H:%M"), 'Пользователь ' + message.from_user.first_name, message.from_user.id, 'написал следующее: ' + message.text, file=botlogfile)
    botlogfile.close()
    start(message)


bot.infinity_polling()

