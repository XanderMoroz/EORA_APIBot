# EORA_APIBot

## Описание проекта

EORA_APIBot представляет телеграм бота отличающего кота от хлеба. Чтобы принять решение бот ведет диалог с пользователями, задавая ему вопросы. На основе ответов пользователя бот принимает решение. Бот прошел тестирование автоматическое(unittest) и ручное тестирование. К боту прилагается асинхронный backend-сервис для хранения всей переписки пользователей с ботом. Переписка доступна для чтения, редактирования и удаления. Бот доступен по адресу: [BreadOrCatbot](https://t.me/BreadOrCatbot)

## Стек технологий 

В ходе создания проекта применялись различные инстументы и технологии. Они представлены ниже:

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![PyCharm](https://img.shields.io/badge/pycharm-143?style=for-the-badge&logo=pycharm&logoColor=black&color=black&labelColor=green)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![Markdown](https://img.shields.io/badge/markdown-%23000000.svg?style=for-the-badge&logo=markdown&logoColor=white)

## Краткая документация API

Объектом сервиса и базы данных выступает сообщение(TGMessage). Он имеет следующий вид: 
```sh
{
  "id": 0,
  "chat_id": 0,
  "task": "string"
}
```
Объект имеет три поля: идентификатор сообщения(id), идентификатор диалога(chat_id) и текст сообщения(text). Работа с объектами осуществляется по следующим эндпоинтам: 

Method | HTTP request | Description
------------- | ------------- | -------------
[**/create_message**] | **POST** /tgmessage | Добавление нового сообщения.
[**/read_message**] | **GET** /tgmessage/{id} |  Извлечение сообщения по ID.
[**/update_message**] | **PUT** /tgmessage/{id} | Редактирование сообщения по ID.
[**/delete_message**] | **DELETE** /tgmessage/{id} | Удаление поста.
[**/tgmessages**] | **GET** read_message_list | Извлечение всех сообщений списком.

Исчерпывающую информацию по работе API можно получить после запуска по адресу http://127.0.0.1:8000/docs
Документация соответствует стандарту OpenAPI.

## Инструкция по установке для среды Windows или OS (используйте терминал)

1. Клонируете репозиторий
```sh
git clone https://github.com/XanderMoroz/EORA_APIBot.git
```
2. Уставливаете, распаковываете и активируете виртуальное окружение (virtual environment)
```sh
pip install virtualenv

python -m venv env  

.\env\Scripts\activate  
```
3. Уставливаете зависимости проекта. Их всего 4 (fastapi, telebot, sqlalchemy, requests). Можно вручную или командой:
```sh
pip install fastapi sqlalchemy telebot requests
```
4. Запускаете API:
```sh
uvicorn main:app --reload 
```
5. Открываете второй терминал для запуска параллельного процесса. Переходите в директроию "telebot" и запускаете бота(CatOrBreadBot.py):
```sh
cd telebot

python CatOrBreadBot.py  
```
6. Общайтесь с ботом и наблюдайте работу сервиса. Наслаждайтесь результатом)

## Лицензия

MaffinWare

## Авторы

* [XanderMoroz](https://https://github.com/XanderMoroz/) - *Все работы*
