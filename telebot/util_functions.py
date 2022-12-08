import config
import requests


user_state = {}                           # Создаем пустой словарь для фиксации состояния пользователя


def get_user_state(user_id):
    """Извлечение «состояния» пользователя. Перечень состояний в config.py """
    try:
        return user_state[user_id]                    # Если словарь не пустой возвращаем значение в виде строки
    except KeyError:                                  # Если такого ключа(user_id) не оказалось,
        return config.StatesOfTalk.BEGIN.value        # возвращаем значение по умолчанию("0"- начало диалога)



def set_user_state(user_id, value):
    """Присвоение текущего «состояния» пользователю"""
    try:
        user_state[user_id] = value             # Пытаемся установить значение "состояние" пользователя
        return True                             # Если все ок возвращаем значение в виде строки
    except:                                     # тут желательно как-то обработать ситуацию
        return False

def send_to_database(chat_id, message):
    try:
        requests.post('http://127.0.0.1:8000/tgmessage', json={'chat_id': chat_id, 'text': message})
        return chat_id, message
    except:
        return False
