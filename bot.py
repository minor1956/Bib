import os
from flask import Flask, request
import telebot
import schedule
import time
import random
from datetime import datetime
from telebot import types

TOKEN = '686570673:AAFfCDwWnjQ-qj8DyNeTYk-Uax7NnVdBHGo'
bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)

VITKA = 827128502
sticker_id = "CAADAgADdQkAAnlc4glquzEKzUMprxYE"
sticker_kk_id = 'CAADAgAD7gEAAsoDBgvfV0-V7BmYhhYE'
name = ["piuuo"]
anya = ['ht']
end = ['shit']
smiles = ['😘', '🥰', '😍', '😚', '☺️', '😻', '😽', '💞', '💋', '♥️']
stories = [
    'h',
    'k',
    '!',
    'o',
    'o',
    'p']



@bot.message_handler(commands=['start'])
def hello(message):
    if message.from_user.username not in name:
        bot.send_message(message.chat.id, '6ОТ СДОХ. УхОдИ!1')
        markup = types.ReplyKeyboardMarkup()
        markup.row('Позвать', '💋')
        markup.row('История из')
        markup.row('сонька', 'Пожелание')
        markup.row('Щ')

        bot.send_message(message.chat.id, 'НОПКА', reply_markup=markup)
       
    else:
        bot.send_message(message.chat.id, 'Ты не!')


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):  # Название функции не играет никакой роли, в принципе
    if (message.from_user.username not in name) or message.from_user.username == 'piuuo':
        bot.send_message(message.chat.id, '6ОТ СДОХ. УхОдИ!1')

        def morning():
            bot.reply_to(message, anya[random.randint(0, len(anya) - 1)] + ", доброго тебе утречка, " + end[
                random.randint(0, len(end) - 1)] +
                         smiles[random.randint(0, len(smiles) - 1)])

        def day():
            bot.reply_to(message,
                         anya[random.randint(0, len(anya) - 1)] + ", доброго тебе денёчка, " + end[
                             random.randint(0, len(end) - 1)] +
                         smiles[random.randint(0, len(smiles) - 1)])

        def evening():
            bot.reply_to(message,
                         anya[random.randint(0, len(anya) - 1)] + ", доброго тебе вечерочка, " + end[
                             random.randint(0, len(end) - 1)] +
                         smiles[random.randint(0, len(smiles) - 1)])

        def night():
            bot.reply_to(message, anya[random.randint(0, len(anya) - 1)] + ", доброй тебе ночки, " + end[
                random.randint(0, len(end) - 1)] +
                         smiles[random.randint(0, len(smiles) - 1)])

        if message.from_user.username != 'piuuo':
            bot.send_message(VITKA, message.from_user.first_name + " написала: " + message.text + ' ' + str(message.chat.id))
        if message.text == 'Позвать' and message.from_user.username != 'piuuo':
            bot.send_message(VITKA, 'зовёт!')
            bot.send_message(message.chat.id, 'Позвал!')
        elif message.text == '💋' and message.from_user.username != 'piuuo':
            bot.send_sticker(message.chat.id, sticker_id)
        elif message.text == 'История из' and message.from_user.username != 'piuuo':
            bot.send_message(message.chat.id, stories[random.randint(0, len(stories) - 1)])
        elif message.text == 'сонька' and message.from_user.username != 'piuuo':
            try:
                bot.send_photo(message.chat.id, 'https://random.cat/view/' + str(random.randint(1, 1677)))
            except Exception as e:
                bot.send_message(VITKA, 'Ошибка в')  
        else:
            if str(datetime.now().time())[0] == '0':
                if str(datetime.now().time())[1] < '3':
                    night()
                elif '3' <= str(datetime.now().time())[1] < '9':
                    morning()
                else:
                    day()
            elif str(datetime.now().time())[0] == '1':
                if str(datetime.now().time())[1] < '5':
                    day()
                else:
                    evening()
            else:
                if str(datetime.now().time())[1] < '1':
                    evening()
                else:
                    night()

    else:
        if message.from_user.username != 'piuuo':
            bot.send_message(VITKA, message.from_user.first_name + " написала: " + message.text)
        bot.send_message(message.chat.id, 'Ты!')


@bot.message_handler(content_types=['sticker'])
def sticker_message(message):
    if message.from_user.username in name:
        bot.send_sticker(message.chat.id, sticker_kk_id)
    else:
        if message.from_user.username != 'piuuo':
            bot.send_message(VITKA, message.from_user.first_name + " прислал(a) стикер")
        bot.send_message(message.chat.id, 'Ты не!')


@bot.message_handler(content_types=['photo'])
def photo_message(message):
    if message.from_user.username in name:
        bot.reply_to(message, 'О!')
    else:
        if message.from_user.username != 'piuuo':
            bot.send_message(VITKA, message.from_user.first_name + " прислала фото")
        bot.send_message(message.chat.id, 'Ты !')


@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://bot681.herokuapp.com/' + TOKEN)
    return "!", 200


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
