from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class SentimentInput(BaseModel):

    sender_id: str
    chat_code: str

# seggreate time needed to UPGRADE to a more complex analytics system in the future
class EmployeeSentimentAnalytics(BaseModel):
    
    employee_id: str
    average_score: float
    sentiment: int
    # total_chats: int 
    created_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True