from fastapi import APIRouter
from fastapi import Depends, status
from sqlalchemy.orm import Session
from pydantic import BaseModel

from app.schemas.sentiment_schema import (
    SentimentInput,
    EmployeeSentimentAnalytics
)

from app.services.sentiment_service import (
    analyse_sentiment,
    calculate_aggregate_sentiment
)

from app.repositories.sentiment_repository import (
    save_sentiment,
    get_employee_sentiments
)

from app.repositories.chat_repository import get_chat_by_code

from app.database.db import SessionLocal


router = APIRouter()


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


# new request model of Base
class EmployeeAnalyticsRequest(BaseModel):

    employee_id: str


@router.post(
    "/predict",
    status_code=status.HTTP_200_OK
)
def predict(
    data: SentimentInput,
    db: Session = Depends(get_db)
):

    chat = get_chat_by_code(
        db,
        data.chat_code,
        data.sender_id
    )

    if not chat:

        return {
            "error": "Chat not found"
        }

    result = analyse_sentiment(
        chat["chat_messages"]
    )

    saved_data = save_sentiment(
        db,
        chat["sender_id"],
        chat["chat_code"],
        result
    )

    return {

        "sentiment_id": str(
            saved_data.sentiment_id
        ),

        "employee_id": saved_data.employee_id,

        "chat_code": saved_data.chat_code,

        "score": saved_data.score,

        "context": chat["chat_messages"],

        "sentiment": saved_data.sentiment,

        "created_at": saved_data.created_at
    }



#--------------------------------------------------#

#testing endpoint to get employee analytics not for production use
# POST
@router.post(
    "/analytics/employee",
    response_model=EmployeeSentimentAnalytics,
    status_code=status.HTTP_200_OK
)
def get_employee_analytics(

    request: EmployeeAnalyticsRequest,

    db: Session = Depends(get_db)

):

    sentiments = get_employee_sentiments(

        db,

        request.employee_id
    )

    if not sentiments:

        return {

            "employee_id": request.employee_id,

            "average_score": 0.0,

            "sentiment": 0,

            "created_at": None
        }

    analytics = calculate_aggregate_sentiment(

        sentiments
    )

    return {

        "employee_id": request.employee_id,

        "average_score": analytics["average_score"],

        "sentiment": analytics["sentiment"],

        "created_at": sentiments[-1].created_at
    }