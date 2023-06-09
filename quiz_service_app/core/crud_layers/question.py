from typing import Union

from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from core.models.models import Question
from core.schemas.question import QuestionSave


async def add_new_question(db: AsyncSession, question: dict) -> Question:
    new_question = Question(
        question_id=question.get('id'),
        question_text=question.get('question_text'),
        answer_text=question.get('answer_text'),
        created_at=question.get('created_at'),
    )
    db.add(new_question)
    await db.commit()
    return new_question


async def select_last_row(db: AsyncSession) -> Union[Question, None]:
    query = select(Question).order_by(Question.question_id.desc())
    last_question = await db.execute(query)

    return last_question.first()


async def get_question_by_id(db: AsyncSession, question_id: str) -> Union[int, None]:
    query = select(Question).where(Question.question_id == question_id)
    result = await db.execute(query)
    return result.scalar_one_or_none()