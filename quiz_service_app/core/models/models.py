import datetime

from sqlalchemy import String, Integer
from sqlalchemy.dialects.postgresql import TIMESTAMP
from sqlalchemy.orm import mapped_column, Mapped

from core.database import Base


class Question(Base):
    __tablename__ = 'questions'

    question_id: Mapped[int] = mapped_column(Integer, primary_key=True,nullable=False)
    question_text: Mapped[str] = mapped_column(String, nullable=False)
    answer_text: Mapped[str] = mapped_column(String, nullable=False)
    create_at: Mapped[datetime.datetime] = mapped_column(TIMESTAMP, nullable=False)
