from bot.bot import Bot
from bot.handler import MessageHandler

TOKEN = "" #вставьте сюда ваш токен от Метабота

bot = Bot(token=TOKEN)


def message_cb(bot, event):
    #отправляем сообщение туда, откуда его получили (event.fromChat) с тем же текстом (event.text)
    bot.send_text(chat_id=event.from_chat, text=event.text)

def main():
    #хэндлер для любого сообщения
    bot.dispatcher.add_handler(MessageHandler(callback=message_cb))
    bot.start_polling()
    bot.idle()
    
if __name__ == "__main__":
    main()
