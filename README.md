<img src="https://github.com/nightadmin/standart-icq-bot/blob/master/logo.png" width="100" height="100">

# 🐍 standart-icq-bot

Официальная библиотека к ICQ New Bot API на Python. Перевод: [@nightadmin](https://vk.com/na_official)

# Содержание:
- [Описание](#описание)
- [Начало работы](#начало-работы)
- [Установка](#установка)
- [Описание API](#описание-API)

# Описание

Эта библиотека является интерфейсом ICQ New Bot API и поддерживается на версиях Python 2.7, 3.4, 3.5 и 3.6.

# Начало работы

* Создайте собственного бота командой /newbot <a href="https://icq.com/people/70001">Метаботу</a> и следуйте инструкциям бота.
    >Внимание: Бот может писать только тем людям, у которых он есть в списке контактов, то есть он не может первым начать диалог с пользователем.
* Вы можете создать свой ICQ-сервер для API, тогда смените адрес хоста на свой при объявлении класса Bot().
    > Пример: Bot(token=TOKEN, name=NAME, version=VERSION, api_url_base="https://example.com"), стандартный сервер ICQ: https://api.icq.net/bot/v1
* Если вы клиент корпоративного сервиса Myteam, вы можете включить флаг "is_myteam=True" для получения дополнительных возможностей при объявлении класса Bot().
    > Пример: Bot(token=TOKEN, name=NAME, is_myteam=True), по умолчанию флаг имеет значение False.


> Пример бота, который использует все методы из библиотеки: [/example/test_bot.py](https://github.com/nightadmin/standart-icq-bot/blob/master/example/test_bot.py) 

# Установка
Установите, используя утилиту pip:
```bash
pip3 install --upgrade mailru-im-bot
```

Или клонируйте с GitHub:
```bash
git clone https://github.com/nightadmin/standart-icq-bot.git
cd standart-icq-bot
python setup.py install
```

# Описание API
<ul>
    <li><a href="https://icq.com/botapi/">icq.com/botapi/</a></li>
    <li><a href="https://agent.mail.ru/botapi/">agent.mail.ru/botapi/</a></li>
</ul>
