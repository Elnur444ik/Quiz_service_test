from main import app
from v1.endpoints.quiz_service import router as question_router

app.include_router(question_router)
