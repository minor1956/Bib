import os
from flask import Flask, request
import telebot
import schedule
import time
import random
from datetime import datetime

TOKEN = '686570673:AAFfCDwWnjQ-qj8DyNeTYk-Uax7NnVdBHGo'
bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)

ok = False
name = ["piuuo", "black_list_jpg"]
anya = ['Анна', 'Аня', 'Анечка', 'Анюта', 'Анюточка', 'Аннушка', 'Анюточечка', 'Анюша', 'Анюшенька', 'Анюшечка']
end = ['киса', 'кисонька', 'кисунечка', 'кисонька', 'кисулечка', 'кисуленька', 'солнышко', 'деточка', 'детка']
smiles = ['😘', '🥰', '😍', '😚', '☺️', '😻', '😽', '💞', '💋', '♥️']


@bot.message_handler(commands=['start', 'restart'])
def hello(message):
    if message.from_user.username in name:
        global ok
        ok = True
        bot.send_message(message.chat.id, 'Привет, Аня)')

        def morning():
            bot.send_message(message.chat.id, anya[random.randint(0, len(anya) - 1)] + ", доброго тебе утречка, " + end[
                random.randint(0, len(end) - 1)] +
                             smiles[random.randint(0, len(smiles) - 1)])

        def day():
            bot.send_message(message.chat.id,
                             anya[random.randint(0, len(anya) - 1)] + ", доброго тебе денёчка, " + end[
                                 random.randint(0, len(end) - 1)] +
                             smiles[random.randint(0, len(smiles) - 1)])

        def evening():
            bot.send_message(message.chat.id,
                             anya[random.randint(0, len(anya) - 1)] + ", доброго тебе вечерочка, " + end[
                                 random.randint(0, len(end) - 1)] +
                             smiles[random.randint(0, len(smiles) - 1)])

        def night():
            bot.send_message(message.chat.id, anya[random.randint(0, len(anya) - 1)] + ", доброй тебе ночки, " + end[
                random.randint(0, len(end) - 1)] +
                             smiles[random.randint(0, len(smiles) - 1)])

        if len(schedule.jobs) != 0:
            for job in schedule.jobs:
                schedule.cancel_job(job)
        schedule.every().day.at("05:00").do(morning)
        schedule.every().day.at("09:00").do(day)
        schedule.every().day.at("15:00").do(evening)
        schedule.every().day.at("21:00").do(night)
        # schedule.every(2).seconds.do(morning)
        # schedule.every(4).seconds.do(day)
        # schedule.every(6).seconds.do(evening)
        # schedule.every(7).seconds.do(night)
        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        bot.send_message(message.chat.id, 'Ты не Анечка!')


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):  # Название функции не играет никакой роли, в принципе
    if message.from_user.username in name:
        bot.reply_to(message, '😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘')
    else:
        bot.send_message(message.chat.id, 'Ты не Анечка!')


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
