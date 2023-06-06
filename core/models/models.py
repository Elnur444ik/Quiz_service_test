import uuid
from sqlalchemy import Column, String, Integer
from sqlalchemy.dialects.postgresql import UUID, TIMESTAMP
from core.models.database import Base


# Base: DeclarativeMeta = declarative_base()


class Question(Base):
    __tablename__ = 'question'

    question_id = Column(Integer, primary_key=True,nullable=False, unique=True)
    question_text = Column(String, nullable=False)
    answer_text = Column(String, nullable=False)
    create_at = Column(TIMESTAMP, nullable=False)
