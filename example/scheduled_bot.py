import schedule
import time
from bot.bot import Bot

TOKEN = "" #вставьте сюда ваш токен от Метабота
bot = Bot(token=TOKEN)

chats_to_send_notifications = [
    "na_group",  # ник чата для рассылки
    "AoLFuNFynm67V2xGFX000",  # штамп приватной группы
    "night_admin",  # ник человека
    "68250238000@chat.agent"  # стандартный chatId
]
text_to_send = "Эй, все идем домой! Ночь на дворе!"

#делаем рассылку циклом
def send_alert():
    for chat in chats_to_send_notifications:

        bot.send_text(chat_id=chat, text=text_to_send)

#обратите внимание: время локальное, то есть то, что установлено на сервере (в регионе сервера)
schedule.every().day.at("21:00").do(send_alert)
while True:
    schedule.run_pending()
    time.sleep(1)

bot.idle()
bot.startPolling()
