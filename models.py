from sqlalchemy import Column, Integer, String
from database import Base

# Define To Do class inheriting from Base
class TGMessage(Base):
    __tablename__ = 'tg_messages'
    id = Column(Integer, primary_key=True)
    chat_id = Column(Integer)
    text = Column(String(256))