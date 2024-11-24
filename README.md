<a id="readme-top"></a>

[![Telegram][telegram-shield]][telegram-url]
[![Python][Python.com]][Python-url]

<br />
<div align="center">
  <a href="https://t.me/Tverse">
    <img src="https://i.ibb.co/Q6Lwvdt/photo-2024-11-18-23-50-52-modified.png" alt="TinyVerse Logo" width="100" height="100">
  </a>

<h3 align="center">Auto-farming <a href="https://t.me/TVERSE">@TVERSE</a></h3>
  <p align="center">
    Автоматическая ферма на <a href="https://t.me/TVERSE">@TVERSE</a>
    <br />
  </p>
</div>




[![TVerse][product-screenshot]](https://i.ibb.co/C8sbzRY/image.png)

Автоматизированный скрипт/ферма на TVERSE, поддерживающий авто-сбор/авто-покупку звезд/реферальную систему.


### Особенности:

- Многопоточность
- Пользовательские настройки для работы с сессиями
  - Привязка прокси
  - Привязка юзер-агента
- Авто-вход
- Авто-сбор
- Авто-реф
- Авто-покупка звезд
- Авто-создание галактики


## Ручная установка

### Windows

1. Склонируйте репозиторий
   ```sh
   git clone https://github.com/mxtadone/tverse.git
   ```
2. Создайте виртуальное окружение
   ```sh
   python -m venv venv
   ```
3. Активируйте виртуальное окружение
   ```sh
   venv\Scripts\activate
   ```
4. Установите необходимые библиотеки в виртуальном окружении
   ```sh
   pip install -r requirements.txt
   ```
5. Запустите скрипт
   ```sh
   python main.py
   ```
   


### Linux

1. Склонируйте репозиторий
   ```sh
   git clone https://github.com/mxtadone/tverse.git
   ```
2. Создайте виртуальное окружение
   ```sh
   python3 -m venv venv
   ```
3. Активируйте виртуальное окружение
   ```sh
   source venv/bin/activate
   ```
4. Установите необходимые библиотеки в виртуальном окружении
   ```sh
   pip3 install -r requirements.txt
   ```
5. Запустите скрипт
   ```sh
   python3 main.py
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Использование

Команды:

1. **Запуск фарма**
2. **Создание сессии**


## Персональные настройки аккаунта

Вы можете управлять своей учетной записью или изменять свой прокси-сервер, отредактировав файл «accounts.json», расположенный в папке сеансов.
Вот пример `accounts.json`:

```json
[
  {
    "session_name": "name_example",
    "user_agent": "Mozilla/5.0 (Linux; Android 14) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.165 Mobile Safari/537.36",
    "proxy": "type://user:pass:ip:port"  # "proxy": "" - если вы используете прокси
  }
]
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>


[telegram-shield]: https://img.shields.io/badge/Telegram-29a9eb?style=for-the-badge&logo=telegram&logoColor=white
[telegram-url]: https://telegram.me/mxtadone
[product-screenshot]: https://i.ibb.co/C8sbzRY/image.png
[Python.com]: https://img.shields.io/badge/python%203.10-3670A0?style=for-the-badge&logo=python&logoColor=ffffff
[Python-url]: https://www.python.org/downloads/release/python-3100/
