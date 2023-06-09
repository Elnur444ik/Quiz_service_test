FROM python:3.9-alpine3.16 #проверить
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install -r /code/requirements.txt
COPY ./quiz_service_app code/quiz_service_app
WORKDIR code/quiz_service_app
CMD gunicorn main:app --bind=0.0.0.0:8000