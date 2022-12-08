from pydantic import BaseModel

# Create TGMessage Schema (Pydantic Model)
class TGMessageCreate(BaseModel):
    chat_id: int
    task: str


# Complete TGMessage Schema (Pydantic Model)
class TGMessage(BaseModel):
    id: int
    chat_id: int
    task: str

    class Config:
        orm_mode = True
