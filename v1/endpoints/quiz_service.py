import asyncio
from typing import List, Any
import httpx
from fastapi import APIRouter, HTTPException, Depends
from httpx import Response
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, JSON
from core.models.database import get_async_session
from core.models.models import Question
from core.schemas.schema import QuestionCount, QuestionSave

router = APIRouter(
    prefix='/questions',
    tags=['Questions'],
)


async def add_question(question: dict, session: AsyncSession = Depends(get_async_session)):
    # if not Question.filter(Question.question_id == question.get('id')):
    query = select(Question).where(Question.question_id == question.get('id')).exists()
    # result = await session.execute(query)
    print(type(query))
    print(query)
    print('fdsfsdfsdfsdfsdfsdfsdfsdfsdfsdfdsfsdfsdfsdfsdfsdfsdfsdfsdfsdf')
    if not query:
        stmt = Question.insert().values(
            question_id=question.get('id'),
            question_text=question.get('question'),
            answer_text=question.get('answer'),
            created_at=question.get('created_at'),
        )
        await session.execute(stmt)
        await session.commit()

        return True


async def add_questions(data: JSON) -> int:
    added_count = 0
    for question in data:
        if await add_question(question):
            added_count += 1
    return added_count


async def request_questions(count: int) -> JSON:
    async with httpx.AsyncClient() as client:
        url = f"https://jservice.io/api/random?count={count}"
        response = await client.get(url)
        if response.status_code != 200:
            raise HTTPException(
                status_code=response.status_code,
                detail='Ошибка при получении вопросов со стороннего API'
            )
        return response.json()


@router.post('/', response_model=List[QuestionSave])
async def question_count(question_num: QuestionCount, session: AsyncSession = Depends(get_async_session)):
    """Получаем количество вопросов, которые необходимо добавить"""
    count = question_num.count
    query = select(Question).order_by(Question.question_id.desc())
    last_question = await session.execute(query)
    last_question = last_question.first()
    while count > 0:
        data = await request_questions(count)
        added_count = await add_questions(data)
        count -= added_count
    return last_question
