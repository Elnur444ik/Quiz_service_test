import httpx
from fastapi import HTTPException
from sqlalchemy import JSON

from core.crud_layers.question import get_question_by_id, add_new_question


async def add_question(question: dict, session):

    result = await get_question_by_id(session, question.get('id'))

    if not result:
        return await add_new_question(session, question)


async def add_questions(data: JSON, session) -> int:
    added_count = 0
    for question in data:
        if await add_question(question, session):
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
