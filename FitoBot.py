import urllib.request as urllib2
import random
import types
import math
import telebot
bot = telebot.TeleBot('1460887912:AAHe1KqAdkPCeQ7t_L0Ds4nsDxNCJxBuDqI')
@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('/start', "/stop")
    user_markup.row('Кошкодевочка', 'Мемчик')
    user_markup.row('Музяо в лабу', 'Мотивирующая цитата')
    bot.send_message(message.from_user.id, 'Привет,Босс, Чем могу помочь? /start', reply_markup=user_markup)
@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.from_user.id,
                     text="To bring up a summary of biological functions, write concentrations. To see a secret, ask. Authors - a group of guys 4 bibi")

@bot.message_handler(content_types=['text'])
def send_text(message):
    if "привет" in message.text.lower():
        bot.send_message(message.from_user.id,'Назови пароль, амиго')

    if message.text=="Ты сейчас огребешь":
     bot.send_message(message.from_user.id,'Прости, Босс')



import types
import math

с = 0;
msolution = 0;

@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == 'conc':
        bot.send_message(message.from_user.id, "Я посчитаю процентную концентрацию твоего раствора.");
        bot.register_next_step_handler(message, get_msolution);
    else:
        bot.send_message(message.from_user.id, 'Напиши /conc');

def get_msolution(message):
    global msolution;
    msolution = int(message.text)
    bot.send_message(message.from_user.id, 'Введите нужный объем, мл');
    bot.register_next_step_handler(message, get_c);

def get_c(message):
    global c;
    bot.send_message('Введите итоговую процентную концентрацию, %');
    while c == 0:
        try:
            c = int(message.text)
        except Exception:
            bot.send_message(message.from_user.id, 'Введите без символа %');
    bot.send_message(message.from_user.id, 'Масса вещества' + str((c * msolution)/ 100) + 'гр')
bot.polling()
