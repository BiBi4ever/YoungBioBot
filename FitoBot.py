import types
import math
import random
import urllib.request as urllib2
import telebot
import os
import types
import math
import logging

TOKEN = os.environ.get('TOKEN')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('/start', "/stop")
    user_markup.row('Кошкодевочка', 'Мемчик')
    user_markup.row('Музыка', 'Таймер')
    bot.send_message(message.from_user.id, 'Привет,Босс, Чем могу помочь? /start', reply_markup=user_markup)
    bot.register_next_step_handler(message, after_push)
    
def features(message):
    return_row = types.ReplyKeyboardMarkup(True, True)
    return_row.row('Назад')
    if message.text == 'Назад':
          after_push(message)
          return
    if message.text == 'Таймер':
    timer_menu = types.ReplyKeyboardMarkup(True, True)
    timer_menu.row('/set_timer', '/unset_timer')

@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.from_user.id,
                     text="To bring up a summary of biological functions, write concentrations. To see a secret, ask. Authors - a group of guys 4 bibi")

@bot.message_handler(content_types=['text'])
def send_text(message):
    if "привет" in message.text.lower():
        bot.send_message(message.from_user.id,'Назови пароль,амиго')

    if message.text=="Ты сейчас огребешь":
     bot.send_message(message.from_user.id,'Прости,босс')
    
#Команды, которые работают не на 100%
@bot.message_handler(content_types=['text']) #Вставим музычку
def handle_text (message):
    if message.text == 'Музяо в лабу':
        logging.info("Сейчас спою!")
        abspath = os.path.abspath(__file__)
        dirname = os.path.dirname(abspath)
        os.chdir(dirname)
        path = 'Music'
        musicpath = os.listdir(path)
        file = random.choice(musicpath)
        audio = open( path + '/' + file, 'rb')
        caption = 'Хорошей работы!'
        #send_random_audio
        bot.send_audio(message.from_user.id, audio)
        bot.register_next_step_handler(message, after_push)
        #directory = 'D:/Telega/Music'
        #all_files_in_directory = os.listdir(directory)
        #random_file = random.choice(all_files_in_directory)
        #aud = open(directory + '/' +random_file, 'rb')
        #bot.send_chat_action(message.from_user.id, 'upload_audio')
        #bot.send_audio(message.from_user.id, aud)
        #aud.close()
        
#Страшное дело с картинками
@bot.message_handler(regexp="Мем")
def send_mem(message):
    abspath = os.path.abspath(__file__)
    dirname = os.path.dirname(abspath)
    os.chdir(dirname)
    path = 'Mem'
    Mempath = os.listdir(path)
    file = random.choice(Mempath)
    Mem = open( path + '/' + file, 'rb')
    #file_id =  #сейчас подумаю над путем 
    bot.send_photo(message.chat.id, Mem) #Отправляем шутку
    #Оно тоже по любасу не работает, но я могу только плакать, простите




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
