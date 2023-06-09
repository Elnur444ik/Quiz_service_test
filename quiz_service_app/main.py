import uvicorn
from fastapi import FastAPI
from v1.endpoints.quiz_service import router as question_router

app = FastAPI(
    title='quiz_service_app'
)

app.include_router(question_router)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
