import telebot
import schedule
import time
import random

bot = telebot.TeleBot('686570673:AAFfCDwWnjQ-qj8DyNeTYk-Uax7NnVdBHGo')
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
        # schedule.every().day.at("08:00").do(morning)
        # schedule.every().day.at("12:00").do(day)
        # schedule.every().day.at("18:00").do(evening)
        # schedule.every().day.at("00:00").do(night)
        schedule.every(8).seconds.do(morning)
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


if __name__ == '__main__':
    bot.polling(none_stop=True)
