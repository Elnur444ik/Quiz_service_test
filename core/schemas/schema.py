import uuid
from datetime import datetime

from pydantic import BaseModel


class QuestionCount(BaseModel):
    count: int


class QuestionSave(BaseModel):
    table_id: uuid.UUID
    question_id: int
    question_text: str
    answer_text: str
    created_at: datetime

    class Config:
        orm_mode = True
