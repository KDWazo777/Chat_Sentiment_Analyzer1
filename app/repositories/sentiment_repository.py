from app.database.model import EmployeeSentiment
import logging

logger = logging.getLogger(__name__)


def save_sentiment(
    db,
    employee_id,
    chat_code,
    result
):

    try:

        sentiment_data = EmployeeSentiment(

        employee_id=employee_id,

        chat_code=chat_code,

        score=result["score"],

        sentiment=result["sentiment"]
)

        db.add(sentiment_data)

        db.commit()

        db.refresh(sentiment_data)

        return sentiment_data

    except KeyError as ke:

        db.rollback()

        logger.error(
            f"Missing key: {ke}"
        )

        raise ValueError(
            f"Invalid result data structure: Missing {ke}"
        )

    except Exception as e:

        db.rollback()

        logger.error(
            f"Failed to save sentiment for chat : {e}"
        )

        raise

# Function to retrieve sentiments for a specific employee for testing purposes
def get_employee_sentiments(
    db,
    employee_id: str
):
    
    sentiments = db.query(
        EmployeeSentiment
    ).filter(
        EmployeeSentiment.employee_id == employee_id
    ).all()
    
    return sentiments