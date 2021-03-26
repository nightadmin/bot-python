from bot.bot import Bot
from bot.handler import MessageHandler

import logging.config

#сохраняем логи
logging.config.fileConfig("logging.ini")

TOKEN = "" #вставьте сюда ваш токен от Метабота

#добавим флаг is_myteam
bot = Bot(token=TOKEN, api_url_base="", is_myteam=True)


def message_cb(bot, event):
    bot.send_text(chat_id=event.from_chat, text="Привет!")
    resp = bot.create_chat(name="Корпоративный чат")
    bot.send_text(chat_id=event.from_chat, text=resp.json()['sn'])
    #добавим наших коллег в чат
    bot.add_chat_members(chat_id=resp.json()['sn'], members=["user1@myteam.ru", "user2@myteam.ru", "user3@myteam.ru"])
    bot.send_text(chat_id=resp.json()['sn'], text="Добро пожаловать!")
    #удалим их. Они плохо себя вели.
    bot.delete_chat_members(chat_id=resp.json()['sn'], members=["user2@myteam.ru", "user3@myteam.ru"])
    bot.send_text(chat_id=event.from_chat, text="До свидания!")    


def main():
    bot.dispatcher.add_handler(MessageHandler(callback=message_cb))
    bot.start_polling()
    bot.idle()
if 
