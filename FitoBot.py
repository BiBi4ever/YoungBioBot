import urllib.request as urllib2
import random
import types
import math
import telebot

TOKEN = os.environ.get('TOKEN')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('/start', "/stop")
    user_markup.row('Кошкодевочка', 'Мемчик')
    user_markup.row('Музяо в лабу', 'Мотивирующая цитата')
    bot.send_message(message.from_user.id, 'Привет,Босс, Чем могу помочь? /start', reply_markup=user_markup)
@bot.message_handler(content_types=['text']) #Вставим музычку
def handle_text (message):
    if message.text == 'Музяо в лабу':
        directory = 'D:/Telega/Music'
        all_files_in_directory = os.listdir(directory)
        random_file = random.choice(all_files_in_directory)
        audio = open(directory + '/' + random_file, 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_audio')
        bot.send_audio(message.from_user.id, audio)
        aud.close()
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

import telebot
from bs4 import BeautifulSoup
import requests

#Новостная функция
@bot.message_handler(content_types = ['text'])
def handle(message):
	URL = 'https://nplus1.ru/rubric/biology'
	HEADERS = {
		'User-Agent' : 'Mozilla / 5.0 (Windows NT 6.1) AppleWebKit / 537.36 (KHTML, например Gecko) Chrome / 89.0.4389.90 Safari / 537.36'
	}

	response = requests.get(URL, headers = HEADERS)
	soup = BeautifulSoup(response.content, 'html.parser')
	texts = soup.findAll('a', 'caption')

	for i in range(len(texts[:-12]), -1, -1):
		txt = str(i + 1) + ') ' + texts[i].text
		#вызов гиперссылки
        bot.send_message(message.chat.id, '<a href="{}">{}</a>'.format(texts[i]['href'], txt), parse_mode = 'html')

bot.polling()
