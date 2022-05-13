FROM python:latest

ADD main.py .

RUN pip install fastapi uvicorn pickle numpy json pandas tensorflow texthero matplotlib pickle 

CMD [ "python","main.py" ]