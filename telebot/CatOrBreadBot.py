import telebot
from config import TOKEN, StatesOfTalk, yes_variants, no_variants
from util_functions import get_user_state, set_user_state, send_to_database


bot = telebot.TeleBot(TOKEN)

# Начало диалога
@bot.message_handler(commands=["start"])
def cmd_start(message):
    """Инициализация диалога с ботом"""
    # Создаем приветственный текст
    welcome_text = f"Привет, {message.chat.first_name}!\nЯ могу отличить кота от хлеба!\nОбъект перед тобой квадратный? "
    # Отправляем в чат
    bot.send_message(message.chat.id, welcome_text)
    # Отправляем реплику в базу данных через API
    send_to_database(message.chat.id, welcome_text)
    # Устанавливаем пользователю "состояние" первого вопроса
    set_user_state(message.chat.id, StatesOfTalk.FIRST_QUESTION.value)



@bot.message_handler(commands=["reset"])
def cmd_reset(message):
    """Перезапуск диалога с ботом"""
    # Создаем новый приветственный текст
    restart_text = f"Что ж, {message.chat.first_name} начнём по-новой.\n" \
                   f"Я могу отличить кота от хлеба!\n" \
                   f"Объект перед тобой квадратный? "
    # Отправляем в чат
    bot.send_message(message.chat.id, restart_text)
    # Отправляем реплику в базу данных через API
    send_to_database(message.chat.id, restart_text)
    # Устанавливаем пользователю "состояние" первого вопроса
    set_user_state(message.chat.id, StatesOfTalk.FIRST_QUESTION.value)

@bot.message_handler(func=lambda message: get_user_state(message.chat.id) == StatesOfTalk.FIRST_QUESTION.value)
def first_question_handler(message):
    """Обработка первого вопроса: Объект перед тобой квадратный?"""
    # Сохраняем сообщение пользователя в базу данных
    send_to_database(message.chat.id, message.text)
    # Если хоть одна фраза из списка эквивалентов "ДА" входит в ответ пользователя:
    if bool([phrase for phrase in yes_variants if(phrase in message.text.lower())]):
        answer = 'Понял. У него есть уши?'           # Формируем ответ
        bot.send_message(message.chat.id, answer)    # Отправляем ответ в чат
        send_to_database(message.chat.id, answer)    # Отправляем ответ в бд
        # Устанавливаем пользователю "состояние" второго вопроса
        set_user_state(message.chat.id, StatesOfTalk.SECOND_QUESTION.value)

    # Если хоть одна фраза из списка эквивалентов "НЕТ" входит в ответ пользователя:
    elif bool([phrase for phrase in no_variants if(phrase in message.text.lower())]):
        answer = 'Это кот, а не хлеб! Не ешь его!'   # Формируем ответ
        bot.send_message(message.chat.id, answer)    # Отправляем ответ в чат
        send_to_database(message.chat.id, answer)    # Отправляем ответ в бд
        reset = 'Хочешь сначала - нажми /reset.'
        bot.send_message(message.chat.id, reset)
        set_user_state(message.chat.id, StatesOfTalk.BEGIN.value)

    # В остальных случаях - переспрашиваем.
    else:
        answer = 'Я не разобрал ответ. Объект перед тобой квадратный?'
        bot.send_message(message.chat.id, answer)
        send_to_database(message.chat.id, answer)

@bot.message_handler(func=lambda message: get_user_state(message.chat.id) == StatesOfTalk.SECOND_QUESTION.value)
def second_question_handler(message):
    """Обработка второго вопроса: У него есть уши?"""
    # Сохраняем сообщение пользователя в базу данных
    send_to_database(message.chat.id, message.text)
    # Если хоть одна фраза из списка эквивалентов "ДА" входит в ответ пользователя:
    if bool([phrase for phrase in yes_variants if(phrase in message.text.lower())]):
        set_user_state(message.chat.id, StatesOfTalk.BEGIN.value)
        answer = 'Это кот, а не хлеб! Не ешь его!'
        bot.send_message(message.chat.id, answer)
        send_to_database(message.chat.id, answer)
        bot.send_message(message.chat.id, 'Если хочешь попробовать снова - отправь команду /reset.')
    # Если хоть одна фраза из списка эквивалентов "НЕТ" входит в ответ пользователя:
    elif bool([phrase for phrase in no_variants if(phrase in message.text.lower())]):
        answer = 'Это хлеб, а не кот! Ешь его!'
        bot.send_message(message.chat.id, answer)
        send_to_database(message.chat.id, answer)
        bot.send_message(message.chat.id, 'Если хочешь попробовать снова - отправь команду /reset.')
        set_user_state(message.chat.id, StatesOfTalk.BEGIN.value)
    # В остальных случаях - переспрашиваем.
    else:
        answer = 'Я не разобрал ответ. У объекта есть уши?'
        bot.send_message(message.chat.id, answer)
        send_to_database(message.chat.id, answer)


if __name__ == "__main__":
    bot.infinity_polling()

