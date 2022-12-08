from fastapi import FastAPI, status, HTTPException, Depends
from database import Base, engine, SessionLocal
from sqlalchemy.orm import Session
import models
import schemas
from typing import List

# Create the database
Base.metadata.create_all(engine)

# Initialize app
app = FastAPI(title="EORA_FastAPIBot",
              description="Сервис предназначен для сохранения переписки с телеграм-ботом CatOrBreadBot."
                          "Бот доступен по адресу https://t.me/BreadOrCatbot",
              version="0.0.1",
              contact={"name": "XanderMoroz",
                       "url": "https://github.com/XanderMoroz",
                       "email": "moroz070688@gmail.com",},
              )

def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

@app.get("/")
def root():
    return "Привет! Я сервис на FastAPI. Я сохраняю переписку с ботом CatOrBreadBot."

@app.post("/tgmessage", response_model=schemas.TGMessage, status_code=status.HTTP_201_CREATED)
def create_message(tgmessage: schemas.TGMessageCreate, session: Session = Depends(get_session)):

    # create an instance of the TGMessage database model
    tgmessagedb = models.TGMessage(chat_id = tgmessage.chat_id, text = tgmessage.text)

    # add it to the session and commit it
    session.add(tgmessagedb)
    session.commit()
    session.refresh(tgmessagedb)

    # return the TGMessage object
    return tgmessagedb



@app.get("/tgmessage/{id}", response_model=schemas.TGMessage)
def read_message(id: int):

    # create a new database session
    session = SessionLocal()

    # get the tgmessage item with the given id
    tgmessage = session.query(models.TGMessage).get(id)

    # close the session
    session.close()

    # check if tgmessage item with given id exists. If not, raise exception and return 404 not found response
    if not tgmessage:
        raise HTTPException(status_code=404, detail=f"tgmessage item with id {id} not found")

    return tgmessage


@app.put("/tgmessage/{id}")
def update_message(id: int, chat_id: int, text: str):

    # create a new database session
    session = SessionLocal()

    # get the tgmessage item with the given id
    tgmessage = session.query(models.TGMessage).get(id)

    # update tgmessage item with the given text (if an item with the given id was found)
    if tgmessage:
        tgmessage.chat_id = chat_id
        tgmessage.text = text
        session.commit()

    # close the session
    session.close()

    # check if tgmessage item with given id exists. If not, raise exception and return 404 not found response
    if not tgmessage:
        raise HTTPException(status_code=404, detail=f"tgmessage item with id {id} not found")

    return tgmessage

@app.delete("/tgmessage/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_message(id: int):

    # create a new database session
    session = SessionLocal()

    # get the tgmessage item with the given id
    tgmessage = session.query(models.TGMessage).get(id)

    # if tgmessage item with given id exists, delete it from the database. Otherwise raise 404 error
    if tgmessage:
        session.delete(tgmessage)
        session.commit()
        session.close()
    else:
        raise HTTPException(status_code=404, detail=f"tgmessage item with id {id} not found")

    return None

@app.get("/tgmessages", response_model = List[schemas.TGMessage])
def read_message_list():
    # create a new database session
    session = SessionLocal()

    # get all tgmessage items
    tgmessage_list = session.query(models.TGMessage).all()

    # close the session
    session.close()

    return tgmessage_list
