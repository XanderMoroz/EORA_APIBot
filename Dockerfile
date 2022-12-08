FROM python:3.8-onbuild

EXPOSE 8000

RUN pip install fastapi sqlalchemy telebot requests
RUN python main.py
RUN cd telebot

CMD ["python", "CatOrBreadBot.py"]
