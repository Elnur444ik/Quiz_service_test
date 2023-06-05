import uuid
from sqlalchemy import Column, String, Integer
from sqlalchemy.dialects.postgresql import UUID, TIMESTAMP
from sqlalchemy.orm import declarative_base, DeclarativeMeta
from core.models.database import Base


# Base: DeclarativeMeta = declarative_base()


class Question(Base):
    __tablename__ = 'question'

    row_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    question_id = Column(Integer, nullable=False, unique=True)
    question_text = Column(String, nullable=False)
    answer_text = Column(String, nullable=False)
    create_at = Column(TIMESTAMP, nullable=False)
