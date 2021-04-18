from __future__ import print_function
#import httplib2

import datetime
import time
import config
import telepot
import schedule

import apiclient 
import discovery
from oauth2client.service_account import ServiceAccountCredentials

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
    user_markup.row('Музыка', 'Напоминания')
    bot.register_next_step_handler(message, after_push)
    bot.send_message(message.from_user.id, 'Привет,Босс, Чем могу помочь? /start', reply_markup=user_markup)
    if message.text == 'Таймер':
        bot.register_next_step_handler(message, timer_menu)

#Впилим календарь
def job():
    print("I'm working...")
    bot = telepot.Bot(config.TOKEN)

    def main():
        credentials = ServiceAccountCredentials.from_json_keyfile_name(config.client_secret_calendar, 'https://www.googleapis.com/auth/calendar.readonly')
        http = credentials.authorize(httplib2.Http())
        service = discovery.build('calendar', 'v3', http=http)

        now = datetime.datetime.utcnow().isoformat() + '2' # '2' indicates UTC time
        now_1day = round(time.time())+86400 #плюс сутки
        now_1day = datetime.datetime.fromtimestamp(now_1day).isoformat() + '2'

        print('Берем 100 событий')
        eventsResult = service.events().list(
            calendarId='kamaelboi221@gmail.com', timeMin=now, timeMax=now_1day, maxResults=100, singleEvents=True,
            orderBy='startTime').execute()
        events = eventsResult.get('items', [])

        if not events:
            print('нет событий на ближайшие сутки')
            bot.sendMessage(message.from_user.id, 'нет событий на ближайшие сутки')
        else:
            msg = '<b>События на ближайшие сутки:</b>\n'
            for event in events:
                start = event['start'].get('dateTime', event['start'].get('date'))
                print(start,' ', event['summary'])
                if not event['description']:
                    print('нет описания')
                    ev_desc = 'нет описания'
                else:
                    print(event['description'])
                    ev_desc = event['description']

                ev_title = event['summary']
                cal_link = '<a href="/%s">Подробнее...</a>'%event['htmlLink']
                ev_start = event['start'].get('dateTime')
                print (cal_link)
                msg = msg+'%s\n%s\n%s\n%s\n\n'%(ev_title, ev_start, ev_desc, cal_link)
                print('===================================================================')
            bot.sendMessage(message.from_user.id, msg, parse_mode='HTML')


    if __name__ == '__main__':
        main()

print('Listening ...')
schedule.every(1).minutes.do(job)
#schedule.every().hour.do(job)
#schedule.every().day.at("11:15").do(job)
#schedule.every().monday.do(job)
#schedule.every().wednesday.at("13:15").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
    
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
    if "привет" in message.text.lower() or "hello" in message.text.lower() or "hi" in message.text.lower():
        bot.send_message(message.from_user.id,'Назови пароль,амиго')
    elif message.text == "Ты сейчас огребешь":
        bot.send_message(message.from_user.id,'Прости,босс')
    else:
        bot.send_message(message.from_user.id, " Я перестал тебя понимать, босс :( Обратись к команде /start или /help ")
        bot.register_next_step_handler(message, handle_start)
    
#Команды, которые работают не на 100%
def after_push(message):
    if message.text == 'Музыка':
        bot.send_message(message.from_user.id, "Сейчас спою!")
        #logging.info("Сейчас спою!")
        abspath1 = os.path.abspath(__file__)
        dirname1 = os.path.dirname(abspath1)
        os.chdir(dirname1)
        path1 = 'Music'
        music_path = os.listdir(path1)
        file1 = random.choice(music_path)
        audio = open(path1 + '/' + file1, 'rb')
        caption1 = 'Хорошей работы!'
        # send_random_audio
        bot.send_audio(message.from_user.id, audio, caption1)
        bot.register_next_step_handler(message, handle_start)
        #directory = 'D:/Telega/Music'
        #all_files_in_directory = os.listdir(directory)
        #random_file = random.choice(all_files_in_directory)
        #aud = open(directory + '/' +random_file, 'rb')
        #bot.send_chat_action(message.from_user.id, 'upload_audio')
        #bot.send_audio(message.from_user.id, aud)
        #aud.close()
    elif message.text == 'Мемчик':
        abspath2 = os.path.abspath(__file__)
        dirname2 = os.path.dirname(abspath2)
        os.chdir(dirname2)
        path2 = 'Mem'
        mempath = os.listdir(path2)
        file2 = random.choice(mempath)
        mem = open(path2 + '/' + file2, 'rb')
        bot.send_photo(message.chat.id, mem)
        bot.register_next_step_handler(message, handle_start)
    elif message.text == 'Кошкодевочка':
        abspath3 = os.path.abspath(__file__)
        dirname3 = os.path.dirname(abspath3)
        os.chdir(dirname3)
        path3 = 'Catgirl'
        catpath = os.listdir(path3)
        file3 = random.choice(catpath)
        photo = open(path3 + '/' + file3, 'rb')
        caption3 = 'А теперь за работу!'
        bot.send_photo(message.chat.id, photo, caption3)
        bot.register_next_step_handler(message, handle_start)   
        
#Страшное дело с картинками
#@bot.message_handler(regexp="Мем")
#def send_mem(message):
    #abspath = os.path.abspath(__file__)
    #dirname = os.path.dirname(abspath)
    #os.chdir(dirname)
    #path = 'Mem'
    #Mempath = os.listdir(path)
    #file = random.choice(Mempath)
    #Mem = open( path + '/' + file, 'rb')
    #file_id =  #сейчас подумаю над путем 
    #bot.send_photo(message.chat.id, Mem) #Отправляем шутку
    #Оно тоже по любасу не работает, но я могу только плакать, простите




c = 0
msolution = 0

def start_conc(message):
    if message.text == '/conc':
        bot.send_message(message.from_user.id, "Я могу посчитать, сколько сухого вещества (в граммах) потребуется тебе для приготовления раствора с определенной процентной концентрацией.  "
                                               "Введи нужный объем раствора, мл.  "
                                               "Пожалуйста, используй точку в качестве разделителя знаков, я маленький бот и еще не знаю как по-другому :)")

        bot.register_next_step_handler(message, get_msolution)
    else:
        bot.send_message(message.from_user.id, 'Напиши /conc')

def get_msolution(message):
    global msolution
    msolution = float(message.text)
    print(msolution)
    bot.send_message(message.from_user.id, 'Введи процентную концентрацию раствора, которая тебе нужна, %')
    bot.register_next_step_handler(message, get_c)

def get_c(message):
    global c
    while c == 0:
        try:
            c = float(message.text)
        except Exception:
            bot.send_message(message.from_user.id, 'Введи без символа %')
            break

    bot.send_message(message.from_user.id, 'Итого, тебе нужно ' + str((float(c) * float(msolution))/ 100) + ' гр')
bot.polling()
