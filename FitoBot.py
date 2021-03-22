import urllib.request as urllib2
import random
import types
import math
import telebot
import os
import json
from bs4 import BeautifulSoup
import requests

TOKEN = os.environ.get('TOKEN')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('/start', "/stop")
    user_markup.row('Музяо в лабу', 'Мотивирующая цитата')
    bot.send_message(message.from_user.id, 'Привет,Босс, Чем могу помочь? /start', reply_markup=user_markup)
@bot.message_handler(content_types=['text']) #Вставим музычку
def handle_text (message):
    if message.text == 'Музяо в лабу':
      abspath = os.path.abspath(__file__)
      dirname = os.path.dirname(abspath)
      os.chdir(dirname)
      path = 'Music'
      musicdirectory = os.listdir(path)
      file = random.choice(musicdirectory)
      audio = open( path + '/' + file, 'rb')
      bot.send_audio(message.from_user.id, audio)
      bot.send_audio(message.from_user.id, "FILEID")
        #directory = 'D://Telega/Music'
        #all_files_in_directory = os.listdir(directory)
        #random_file = random.choice(all_files_in_directory)
        #audio = open(directory + '/' + random_file, 'rb')
        #bot.send_chat_action(message.from_user.id, 'upload_audio')
        #bot.send_audio(message.from_user.id, audio)
        #aud.close()
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
bot.polling()
