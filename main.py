import uvicorn
from fastapi import FastAPI

app = FastAPI(
    title='quiz_service'
)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
