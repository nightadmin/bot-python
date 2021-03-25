<img src="https://github.com/mail-ru-im/bot-python/blob/master/logo.png" width="100" height="100">

# 🐍 standart-icq-bot

Официальная библиотека к ICQ New Bot API на Python. Перевод: [@nightadmin](https://vk.com/na_official)

# Содержание:
- [Описание](#introduction)
- [Начало работы](#getting-started)
- [Установка](#installing)
- [Описание API](#api-description)

# Описание

This library provides complete Bot API 1.0 interface and compatible with Python 2.7, 3.4, 3.5 and 3.6.

# Начало работы

* Create your own bot by sending the /newbot command to <a href="https://icq.com/people/70001">Metabot</a> and follow the instructions.
    >Note: a bot can only reply after the user has added it to his contact list, or if the user was the first to start a dialogue.
* You can configure the domain that hosts your ICQ server. When instantiating the Bot class, add the address of your domain.
    > Example: Bot(token=TOKEN, name=NAME, version=VERSION, api_url_base="https://api.icq.net/bot/v1"), by default we use the domain: https://api.icq.net/bot/v1
* If you are Myteam client, you can add flag "is_myteam=True", when instantiating the Bot class. This will let you use additional chat methods.
    > Example: Bot(token=TOKEN, name=NAME, is_myteam=True), by default it is False.


> An example of how to use the framework can be seen in example/test_bot.py 

# Установка
Установите, используя утилиту pip:
```bash
pip3 install --upgrade mailru-im-bot
```

Или клонируйте с GitHub:
```bash
git clone https://github.com/mail-ru-im/bot-python.git
cd bot-python
python setup.py install
```

# API description
<ul>
    <li><a href="https://icq.com/botapi/">icq.com/botapi/</a></li>
    <li><a href="https://agent.mail.ru/botapi/">agent.mail.ru/botapi/</a></li>
</ul>
