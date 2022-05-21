FROM python:3.9.7

ENV PORT=$PORT

RUN pip install -r requirements.txt

COPY . /app

EXPOSE $PORT

CMD uvicorn main:app --host 0.0.0.0 --port $PORT