import io
import json
import logging.config
from time import sleep
import sys
from bot.bot import Bot
from bot.filter import Filter
from bot.handler import HelpCommandHandler, UnknownCommandHandler, MessageHandler, FeedbackCommandHandler, \
    CommandHandler, NewChatMembersHandler, LeftChatMembersHandler, PinnedMessageHandler, UnPinnedMessageHandler, \
    EditedMessageHandler, DeletedMessageHandler, StartCommandHandler, BotButtonCommandHandler

if sys.version_info[0] == 3:
    from gtts import gTTS

logging.config.fileConfig("logging.ini")
log = logging.getLogger(__name__)

NAME = ""
VERSION = "0.0.0"
TOKEN = "XXX.XXXXXXXXXX.XXXXXXXXXX:XXXXXXXXX"
OWNER = "XXXXXXXXX"
TEST_CHAT = "XXXXX"
TEST_USER = "XXXXX"
API_URL = "https://api.icq.net/bot/v1"


def start_cb(bot, event):
    bot.send_text(chat_id=event.data['chat']['chatId'], text="Привет! Давай начнем работу!")


def help_cb(bot, event):
    bot.send_text(chat_id=event.data['chat']['chatId'], text="Команда помощи. Чтобы отключить системное уведомление, отправьте Метаботу команду /sethelpenabled => Disabled.")


def test_cb(bot, event):
    bot.send_text(chat_id=event.data['chat']['chatId'], text="Пользователь написал: {}".format(event.data['text']))


def unknown_command_cb(bot, event):
    user = event.data['chat']['chatId']
    (command, command_body) = event.data["text"].partition(" ")[::2]
    bot.send_text(
        chat_id=user,
        text="Неизвестная команда '{message}' с телом '{command_body}' получена от '{source}'.".format(
            source=user, message=command[1:], command_body=command_body
        )
    )


def private_command_cb(bot, event):
    bot.send_text(chat_id=event.data['chat']['chatId'], text="Пользовательская команда: {}".format(event.data['text']))


def new_chat_members_cb(bot, event):
    bot.send_text(
        chat_id=event.data['chat']['chatId'],
        text="Добро пожаловать в чат! {users}, прочитайте правила!".format(
            users=", ".join([u['userId'] for u in event.data['newMembers']])
        )
    )


def left_chat_members_cb(bot, event):
    bot.send_text(
        chat_id=event.data['chat']['chatId'],
        text="Пользователь(и) {users} покинули группу.".format(
            users=", ".join([u['userId'] for u in event.data['leftMembers']])
        )
    )


def pinned_message_cb(bot, event):
    bot.send_text(chat_id=event.data['chat']['chatId'], text="Сообщение с msgId = {} закреплено.".format(event.data['msgId']))


def unpinned_message_cb(bot, event):
    bot.send_text(chat_id=event.data['chat']['chatId'], text="Сообщение с msgId = {} откреплено.".format(event.data['msgId']))


def edited_message_cb(bot, event):
    bot.send_text(chat_id=event.data['chat']['chatId'], text="Сообщение с msgId = {} было редактировано.".format(event.data['msgId']))


def deleted_message_cb(bot, event):
    bot.send_text(chat_id=event.data['chat']['chatId'], text="Сообщение с msgId = {} удалено.".format(event.data['msgId']))
    print("Этот хэндлер был удален по многочисленным просьбам пользователей. Эта функция никогда не сработает.")


def message_with_bot_mention_cb(bot, event):
    bot.send_text(chat_id=event.data['chat']['chatId'], text="Сообщение с упоминанием бота.")


def mention_cb(bot, event):
    bot.send_text(
        chat_id=event.data['chat']['chatId'],
        text="Пользователи {users} были упомянуты.".format(
            users=", ".join([p['payload']['userId'] for p in event.data['parts']])
        )
    )


def reply_to_message_cb(bot, event):
    msg_id = event.data['msgId']
    bot.send_text(
        chat_id=event.data['chat']['chatId'],
        text="Ответил на сообщение с msgId = {}".format(msg_id),
        reply_msg_id=msg_id
    )


def regexp_only_dig_cb(bot, event):
    bot.send_text(chat_id=event.data['chat']['chatId'], text="Регулярное выражение: в сообщении только цифры!")


def file_cb(bot, event):
    bot.send_text(
        chat_id=event.data['chat']['chatId'],
        text="Файлы с {filed} fileId отправлены.".format(
            filed=", ".join([p['payload']['fileId'] for p in event.data['parts']])
        )
    )


def image_cb(bot, event):
    bot.send_text(
        chat_id=event.data['chat']['chatId'],
        text="Найдено сообщение с изображением: {filed} fileId!".format(
            filed=", ".join([p['payload']['fileId'] for p in event.data['parts']])
        )
    )


def video_cb(bot, event):
    bot.send_text(
        chat_id=event.data['chat']['chatId'],
        text="Найдено сообщение с видео с {filed} fileId!".format(
            filed=", ".join([p['payload']['fileId'] for p in event.data['parts']])
        )
    )


def audio_cb(bot, event):
    bot.send_text(
        chat_id=event.data['chat']['chatId'],
        text="Отправлен аудиофайл с {filed} fileId!".format(
            filed=", ".join([p['payload']['fileId'] for p in event.data['parts']])
        )
    )


def sticker_cb(bot, event):
    bot.send_text(chat_id=event.data['chat']['chatId'], text="Твой стикер в сообщении такой смешной!")


def url_cb(bot, event):
    bot.send_text(chat_id=event.data['chat']['chatId'], text="Отправлена ссылка!")


def forward_cb(bot, event):
    bot.send_text(chat_id=event.data['chat']['chatId'], text="Forward was received")


def reply_cb(bot, event):
    bot.send_text(chat_id=event.data['chat']['chatId'], text="Упоминание отправлено")


def message_cb(bot, event):
    bot.send_text(chat_id=event.data['chat']['chatId'], text="Сообщение отправлено!")


def pin_cb(bot, event):
    # бот должен быть админом для выполнения этого действия
    command, command_body = event.data["text"].partition(" ")[::2]
    bot.pin_message(chat_id=event.data['chat']['chatId'], msg_id=command_body)


def unpin_cb(bot, event):
    # бот должен быть админом для выполнения этого действия
    command, command_body = event.data["text"].partition(" ")[::2]
    bot.unpin_message(chat_id=event.data['chat']['chatId'], msg_id=command_body)


def buttons_answer_cb(bot, event):
    if event.data['callbackData'] == "call_back_id_2":
        bot.answer_callback_query(
            query_id=event.data['queryId'],
            text="Хей! Ты нажал кнопку 2.",
            show_alert=True
        )

    elif event.data['callbackData'] == "call_back_id_3":
        bot.answer_callback_query(
            query_id=event.data['queryId'],
            text="Хей! Ты нажал кнопку 3.",
            show_alert=False
        )


def main():
    # создаем инстанс бота
    bot = Bot(token=TOKEN, name=NAME, version=VERSION, api_url_base=API_URL)

    # Регистрация хэндлеров #
    # -------------------- #
    # Хэндлер для команды /start
    bot.dispatcher.add_handler(StartCommandHandler(callback=start_cb))

    # Хэндлер для команды /help
    bot.dispatcher.add_handler(HelpCommandHandler(callback=help_cb))

    # Хэндлер для пользовательской команды /test
    bot.dispatcher.add_handler(CommandHandler(command="test", callback=test_cb))

    # Хэндлер для фидбэка
    bot.dispatcher.add_handler(FeedbackCommandHandler(target=OWNER))

    # Хэндлер для неправильной команды
    bot.dispatcher.add_handler(UnknownCommandHandler(callback=unknown_command_cb))

    # Хэндлер для приватной команды с фильтром по отправителю (сработает только при отправке команды разработчиком бота)
    bot.dispatcher.add_handler(CommandHandler(
        command="restart",
        filters=Filter.sender(user_id=OWNER),
        callback=private_command_cb
    ))

    # Хэндлер для команды "Новый пользователь"
    bot.dispatcher.add_handler(NewChatMembersHandler(callback=new_chat_members_cb))

    # Хэндлер для команды "Пользователь покинул группу"
    bot.dispatcher.add_handler(LeftChatMembersHandler(callback=left_chat_members_cb))

    # Хэндлер для команды "Сообщение закреплено"
    bot.dispatcher.add_handler(PinnedMessageHandler(callback=pinned_message_cb))

    # Хэндлер для команды "Сообщение откреплено"
    bot.dispatcher.add_handler(UnPinnedMessageHandler(callback=unpinned_message_cb))

    # Хэндлер для редактирования сообщения
    bot.dispatcher.add_handler(EditedMessageHandler(callback=edited_message_cb))

    # Хэндлер для удаления сообщения (ОТКЛЮЧЕН, НЕ ИСПОЛЬЗОВАТЬ)
    bot.dispatcher.add_handler(DeletedMessageHandler(callback=deleted_message_cb))

    # Хэндлер для упоминания ботом
    bot.dispatcher.add_handler(MessageHandler(
        filters=Filter.message & Filter.mention(user_id=bot.uin),
        callback=message_with_bot_mention_cb
    ))

    # Хэндлер для упоминания пользователем
    bot.dispatcher.add_handler(MessageHandler(
        filters=Filter.mention() & ~Filter.mention(user_id=bot.uin),
        callback=mention_cb
    ))

    # Хэндлер для текста без файлов
    bot.dispatcher.add_handler(MessageHandler(filters=Filter.text, callback=message_cb))

    # Хэндлер с регулярным выражением: только цифры
    bot.dispatcher.add_handler(MessageHandler(filters=Filter.regexp("^\d*$"), callback=regexp_only_dig_cb))

    # Хэндлер для немедийного файла (например, MarkFomin.txt)
    bot.dispatcher.add_handler(MessageHandler(filters=Filter.data, callback=file_cb))

    # Handlers for other file types
    bot.dispatcher.add_handler(MessageHandler(filters=Filter.image, callback=image_cb))
    bot.dispatcher.add_handler(MessageHandler(filters=Filter.video, callback=video_cb))
    bot.dispatcher.add_handler(MessageHandler(filters=Filter.audio, callback=audio_cb))

    # Хэндлер для стикера
    bot.dispatcher.add_handler(MessageHandler(filters=Filter.sticker, callback=sticker_cb))

    # Хэндлер для ссылки
    bot.dispatcher.add_handler(MessageHandler(filters=Filter.url & ~Filter.sticker, callback=url_cb))

    # Хэндлеры для пересылания и ответа на сообщение соответственно
    bot.dispatcher.add_handler(MessageHandler(filters=Filter.forward, callback=forward_cb))
    bot.dispatcher.add_handler(MessageHandler(filters=Filter.reply, callback=reply_cb))

    # Команда /pin закрепляет сообщение по его msgId:
    # /pin 6752793278973351456
    # 6752793278973351456 - msgId
    # Хэндлер для команды
    bot.dispatcher.add_handler(CommandHandler(command="pin", callback=pin_cb))

    # Send command like this:
    # /unpin 6752793278973351456
    # 6752793278973351456 - msgId
    # Handler for unpin command
    bot.dispatcher.add_handler(CommandHandler(command="unpin", callback=unpin_cb))

    # Starting a polling thread watching for new events from server. This is a non-blocking call
    # ---------------------------------------------------------------------------------------- #
    bot.start_polling()

    # Call bot methods
    # -------------- #
    # Get info about bot
    bot.self_get()

    # Send message
    response = bot.send_text(chat_id=OWNER, text="Hello")
    msg_id = response.json()['msgId']

    # Reply
    bot.send_text(chat_id=OWNER, text="Reply to 'Hello'", reply_msg_id=msg_id)

    # Forward
    bot.send_text(chat_id=OWNER, text="Forward 'Hello'", forward_msg_id=msg_id, forward_chat_id=OWNER)

    # Send binary file
    with io.StringIO() as file:
        file.write(u'x'*100)
        file.name = "file.txt"
        file.seek(0)
        response = bot.send_file(chat_id=OWNER, file=file.read(), caption="binary file caption")
        file_id = response.json()['fileId']

    # Get file info
    bot.get_file_info(file_id=file_id)

    # Send file by file_id
    bot.send_file(chat_id=OWNER, file_id=file_id, caption="file_id file caption")

    # Send file by file_id as reply to message
    bot.send_file(chat_id=OWNER, file_id=file_id, caption="file_id file caption", reply_msg_id=msg_id)

    # Forward file by file_id
    bot.send_file(
        chat_id=OWNER,
        file_id=file_id,
        caption="file_id file caption",
        forward_msg_id=msg_id,
        forward_chat_id=OWNER
    )

    # Send voice file
    if sys.version_info[0] == 3:
        with io.BytesIO() as file:
            gTTS('Hello everybody!').write_to_fp(file)
            file.name = "hello_voice.mp3"
            file.seek(0)
            response = bot.send_voice(chat_id=OWNER, file=file.read())
            hello_voice_file_id = response.json()['fileId']

        # Send voice by file_id
        bot.send_voice(chat_id=OWNER, file_id=hello_voice_file_id)

    # Edit text
    msg_id = bot.send_text(chat_id=OWNER, text="Message to be edited").json()['msgId']
    bot.edit_text(chat_id=OWNER, msg_id=msg_id, text="edited text")

    # Delete message
    msg_id = bot.send_text(chat_id=OWNER, text="Message to be deleted").json()['msgId']
    bot.delete_messages(chat_id=OWNER, msg_id=msg_id)

    # Send typing action
    bot.send_actions(chat_id=OWNER, actions=["typing"])
    sleep(1)
    # Stop typing
    bot.send_actions(chat_id=OWNER, actions=[])

    # Get info about chat
    bot.get_chat_info(chat_id=TEST_CHAT)

    # Get chat admins
    bot.get_chat_admins(chat_id=TEST_CHAT)
    # Get chat members
    bot.get_chat_members(chat_id=TEST_CHAT)
    # Get chat blocked users
    bot.get_chat_blocked_users(chat_id=TEST_CHAT)
    # Get chat pending users
    bot.get_chat_pending_users(chat_id=TEST_CHAT)

    # Block user in chat
    bot.chat_block_user(chat_id=TEST_CHAT, user_id=TEST_USER, del_last_messages=True)
    # Unlock user in chat
    bot.chat_unblock_user(chat_id=TEST_CHAT, user_id=TEST_USER)

    # Chat resolve pending user or everyone
    bot.chat_resolve_pending(chat_id=TEST_CHAT, approve=True, user_id=TEST_USER, everyone=False)

    # Set chat title
    bot.set_chat_title(chat_id=TEST_CHAT, title="TEST TITLE")
    # Set chat about
    bot.set_chat_about(chat_id=TEST_CHAT, about="TEST ABOUT")
    # Set chat title
    bot.set_chat_rules(chat_id=TEST_CHAT, rules="TEST RULES")

    # Send bot buttons
    bot.send_text(chat_id=OWNER,
                  text="Hello with buttons.",
                  inline_keyboard_markup="[{}]".format(json.dumps([
                      {"text": "Action 1", "url": "http://mail.ru"},
                      {"text": "Action 2", "callbackData": "call_back_id_2"},
                      {"text": "Action 3", "callbackData": "call_back_id_3"}
                  ])))

    # Handler for bot buttons reply.
    bot.dispatcher.add_handler(BotButtonCommandHandler(callback=buttons_answer_cb))

    bot.idle()

#если мы вышли из всех сопрограмм, то есть находимся в основной программе, то есть весь код уже обработан, то вызываем функцию, которая начинает работу бота
if __name__ == "__main__":
    main()
