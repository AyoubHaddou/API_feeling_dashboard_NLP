FROM python:3.9.7
ARG port

COPY requirements.txt app/requirements.txt

WORKDIR /app

ENV PORT=6702

RUN pip install -r requirements.txt

EXPOSE $PORT

COPY . /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", '$PORT , "--reload"]