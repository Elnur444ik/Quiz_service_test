import uuid
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID, TIMESTAMP
from sqlalchemy.orm import declarative_base, DeclarativeMeta

Base: DeclarativeMeta = declarative_base()


class Question(Base):
    __tablename__ = 'question'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    question_text = Column(String, nullable=False, unique=True)
    answer_text = Column(String, nullable=False)
    create_at = Column(TIMESTAMP, nullable=False)
