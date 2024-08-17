# Интерфейс для GREEN-API

Этот проект предоставляет простой веб-интерфейс для взаимодействия с GREEN-API, позволяя пользователям выполнять следующие действия:

- **getSettings**: Получить настройки инстанса GREEN-API.
- **getStateInstance**: Проверить текущее состояние инстанса GREEN-API.
- **sendMessage**: Отправить сообщение на указанный номер WhatsApp.
- **sendFileByUrl**: Отправить файл на указанный номер WhatsApp через URL.

## Предварительные требования

- Python 3.x
- Django 4.x
- Библиотека Requests

## Установка

**Клонируйте репозиторий:**

   ```bash
   git clone https://github.com/yourusername/green-api-interface.git
   cd green-api-interface


Установите необходимые зависимости:

pip install -r requirements.txt

Запустите сервер разработки Django:

python local.py runserver
