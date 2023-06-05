import asyncio
from typing import List

import aiohttp
from aiohttp import ClientResponse
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.models.database import get_async_session
from core.models.models import Question
from core.schemas.schema import QuestionCount, QuestionSave

router = APIRouter(
    prefix='/questions',
    tags=['Questions'],
)


async def add_question(question: dict, session: AsyncSession = Depends(get_async_session)) -> bool:
    if not Question.query.filter(Question.question_id == question.get('id')):
        stmt = Question.insert().values(
            question_id=question.get('id'),
            question_text=question.get('question'),
            answer_text=question.get('answer'),
            created_at=question.get('created_at'),
        )
        await session.execute(stmt)
        await session.commit()

        return True


async def add_questions(data: List[dict]) -> int:
    added_count = 0
    for question in data:
        if await add_question(question):
            added_count += 1
    return added_count


async def fetch_content(url, session) -> ClientResponse:
    async with session.get(url, allow_redirect=True) as response:
        if response.status != '200':
            raise HTTPException(
                status_code=response.status,
                detail='Ошибка при получении вопросов со стороннего API'
            )
        return response


async def request_questions(count: int) -> List[dict]:
    url = f'https://jservice.io/api/random?count={count}'
    async with aiohttp.ClientSession() as session:
        data = await fetch_content(url, session).json()
        return data


@router.post('', response_model=List[QuestionSave])
async def question_count(question_num: QuestionCount, session: AsyncSession = Depends(get_async_session)):
    """Получаем количество вопросов, которые необходимо добавить"""
    count = question_num.count
    query = Question.query.order_by(Question.row_id.desc()).first()
    last_question = await session.execute(query)
    while count > 0:
        data = asyncio.run(request_questions(count))
        added_count = await add_questions(data)
        count -= added_count
    return last_question
