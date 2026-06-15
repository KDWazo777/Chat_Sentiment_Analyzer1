from sqlalchemy import Column, Text
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import SmallInteger
from sqlalchemy import TIMESTAMP
from sqlalchemy.sql import func

from sqlalchemy.dialects.postgresql import UUID

from app.database.db import Base


class EmployeeSentiment(Base):

    __tablename__ = "employee_sentiments"

    sentiment_id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=func.gen_random_uuid()
    )

    company_id = Column(
        UUID(as_uuid=True),
        nullable=False,
        server_default=func.gen_random_uuid()
    )

    employee_id = Column(
        String(255),
        nullable=False
    )

    chat_code = Column(
        String(50),
        nullable=False
    )

    score = Column(
        Float,
        nullable=False
    )

    sentiment = Column(
        SmallInteger,
        nullable=False
    )

    created_at = Column(
        TIMESTAMP,
        server_default=func.now()
    )


class EmployeeChat(Base):

    __tablename__ = "employee_chats"

    chat_id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=func.gen_random_uuid()
    )

    sender_id = Column(
        String(20),
        nullable=False
    )

    receiver_id = Column(
        String(20),
        nullable=False
    )

    chat_code = Column(
        String(50),
        nullable=False
    )

    chat_messages = Column(
        Text,
        nullable=False
    )

    created_at = Column(
        TIMESTAMP,
        server_default=func.now()
    )

