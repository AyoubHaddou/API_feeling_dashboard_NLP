FROM python:3.9.7

COPY requirements.txt app/requirements.txt

WORKDIR /API_FEELING_DASHBOARD

RUN pip install -r requirements.txt

COPY . /API_FEELING_DASHBOARD

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80" , "--reload"]