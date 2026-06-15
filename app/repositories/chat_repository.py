from sqlalchemy.orm import Session
from app.database.model import EmployeeChat

def get_chat_by_code(
    db: Session,
    chat_code: str,
    sender_id: str
):

    chats = db.query(
        EmployeeChat
    ).filter(
        EmployeeChat.chat_code == chat_code,
        EmployeeChat.sender_id == sender_id
    ).all()

    if not chats:

        return None

    return {

        "sender_id": chats[0].sender_id,

        "receiver_id": chats[0].receiver_id,

        "chat_code": chat_code,

        "chat_messages": " ".join(

            chat.chat_messages

            for chat in chats
        )
    }