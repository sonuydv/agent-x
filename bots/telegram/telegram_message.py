from typing import Optional, List

from pydantic.v1 import BaseModel


class User(BaseModel):
    id: int
    is_bot: bool
    first_name: str
    username: Optional[str]
    language_code: Optional[str]


class MessageEntity(BaseModel):
    offset: int
    length: int
    type: str


class Chat(BaseModel):
    id: int
    title: Optional[str]
    type: str


class Message(BaseModel):
    message_id: int
    from_: User  # 👈 use alias
    chat: Chat
    date: int
    text: Optional[str]
    entities: Optional[List[MessageEntity]]

    # Use Pydantic's Config to set the alias for 'from_' since telegram returns 'from' which is a reserved keyword in Python
    class Config:
        fields = {"from_": "from"}


class TelegramMessage(BaseModel):
    update_id: int
    message: Message