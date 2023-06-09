import uuid
from datetime import datetime

from pydantic import BaseModel


class QuestionCount(BaseModel):
    count: int


class TunedModel(BaseModel):
    class Config:
        orm_mode = True


class QuestionSave(BaseModel):
    question_id: int
    question_text: str
    answer_text: str
    created_at: datetime

    class Config:
        orm_mode = True
