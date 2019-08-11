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
name = ["piuuo", "black_list_jpg"]
anya = ['Анна', 'Аня', 'Анечка', 'Анюта', 'Анюточка', 'Аннушка', 'Анюточечка', 'Анюша', 'Анюшенька', 'Анюшечка']
end = ['киса', 'кисонька', 'кисунечка', 'кисонька', 'кисулечка', 'кисуленька', 'солнышко', 'деточка', 'детка',
       'сладкая', 'сладенькая']
smiles = ['😘', '🥰', '😍', '😚', '☺️', '😻', '😽', '💞', '💋', '♥️']
stories = [
    'Закупился я как-то пиццей после школы и пошел радостно домой её кушать. Тут меня увидел вредный и голодный одноклассник и побежал за мной, чтобы отобрать пиццу. Так этот лох меня мало того, что не догнал, так еще и телефон свой просрал, пока бежал!',
    'Сижу я на алгебре в 8-м классе, и тут как громыхнёт на весь класс! Это огромный одноклассник пёрнул! Раздались какие-то сдавленные смешки, а учитель сделал вид, что ничего не заметил!',
    'Бежал я классе в 10-м 100 метров. Выбежал сразу после выстрела! Рядом со мной челик бежал, думал всё, жопа, обгонит меня. Так нет, я его обогнал на 0.01 секунды на финише, чему очень обрадовался!!!',
    'Захожу я на урок физры в 7-м классе, поворачиваю голову в сторону, и тут мне со всей силы прилетает мяч прямо в ухо! Я упал и сидел оглушенный пару минут, но потом все прошло.',
    'Иду я на пару линала как-то. Прямо у входа вспоминаю, что забыл пропуск. Обосрался, конечно, и побежал домой. Взял пропуск, бегу на пару. Прибегаю, а ее ОТМЕНИЛИ НАХУЙ!!!!!! Я тогда очень рассторился(((']


# che = ""


@bot.message_handler(commands=['start'])
def hello(message):
    if message.from_user.username in name:
        bot.send_message(message.chat.id, 'Привет, Аня)')
        markup = types.ReplyKeyboardMarkup()
        markup.row('Позвать Витька!', '💋')
        markup.row('История из жития Витька(реальная!!!)')
        markup.row('Кисонька для кисоньки😽')
        bot.send_message(message.chat.id, 'КНОПКА', reply_markup=markup)
        # global che
        # if che == "":
        #     if len(schedule.jobs) != 0:
        #         for job in schedule.jobs:
        #             schedule.cancel_job(job)
        #     # schedule.every().day.at("08:00").do(morning)
        # schedule.every().day.at("12:00").do(day)
        # schedule.every().day.at("18:00").do(evening)
        # schedule.every().day.at("02:17").do(night)
        # schedule.every(2).seconds.do(morning)
        # schedule.every(4).seconds.do(day)

        # schedule.every(6).seconds.do(evening)
        # schedule.every(7).seconds.do(night)
        # che = '1'
        # while che == '1':
        #     try:
        #         schedule.run_pending()
        #         time.sleep(1)
        #     except Exception as e:
        #         # if 'was blocked by the user' in str(e):
        #         print(str(e))
        #         che = ""
    else:
        bot.send_message(message.chat.id, 'Ты не Анечка!')


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):  # Название функции не играет никакой роли, в принципе
    if message.from_user.username in name:

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
            bot.send_message(VITKA, message.from_user.first_name + " написала: " + message.text)
        if message.text == 'Позвать Витька!' and message.from_user.username != 'piuuo':
            bot.send_message(VITKA, 'Аня зовёт!')
            bot.send_message(message.chat.id, 'Позвал Витька!')
        elif message.text == '💋' and message.from_user.username != 'piuuo':
            bot.send_sticker(message.chat.id, sticker_id)
        elif message.text == 'История из жития Витька(реальная!!!)' and message.from_user.username != 'piuuo':
            bot.send_message(message.chat.id, stories[random.randint(0, len(stories) - 1)])
        elif message.text == 'Кисонька для кисоньки😽':  # and message.from_user.username != 'piuuo':
            try:
                bot.send_photo(message.chat.id, 'https://random.cat/view/' + str(random.randint(1, 1677)))
            except Exception as e:
                bot.send_message(VITKA, 'Ошибка отпрвки фотки!!!')
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

        # if message.from_user.username == 'piuuo':
        #     bot.send_message(message.chat.id, str(message.chat.id))

    else:
        if message.from_user.username != 'piuuo':
            bot.send_message(VITKA, message.from_user.first_name + " написала: " + message.text)
        bot.send_message(message.chat.id, 'Ты не Анечка!')


@bot.message_handler(content_types=['sticker'])
def sticker_message(message):
    if message.from_user.username in name:
        bot.send_sticker(message.chat.id, sticker_kk_id)
    else:
        if message.from_user.username != 'piuuo':
            bot.send_message(VITKA, message.from_user.first_name + " прислала стикер")
        bot.send_message(message.chat.id, 'Ты не Анечка!')


@bot.message_handler(content_types=['photo'])
def photo_message(message):
    if message.from_user.username in name:
        bot.reply_to(message, 'Отличное фото!')
    else:
        if message.from_user.username != 'piuuo':
            bot.send_message(VITKA, message.from_user.first_name + " прислала фото")
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
