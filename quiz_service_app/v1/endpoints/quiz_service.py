from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession


from core.crud_layers.question import select_last_row
from core.database import get_async_session
from core.schemas.question import QuestionCount, QuestionSave
from v1.utils.quiz_service import request_questions, add_questions

router = APIRouter(
    prefix='/questions',
    tags=['Questions'],
)


@router.post('/', response_model=List[QuestionSave])
async def question_count(question_num: QuestionCount, session: AsyncSession = Depends(get_async_session)):
    """Получаем количество вопросов, которые необходимо добавить"""
    count = question_num.count

    last_question = await select_last_row(session)

    while count > 0:
        data = await request_questions(count)
        added_count = await add_questions(data, session)
        count -= added_count

    return last_question
