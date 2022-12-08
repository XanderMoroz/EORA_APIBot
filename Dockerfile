FROM python:3.8-onbuild

EXPOSE 8000

RUN pip install -r requirements.txt
RUN python main.py
RUN cd telebot

CMD ["python", "CatOrBreadBot.py"]