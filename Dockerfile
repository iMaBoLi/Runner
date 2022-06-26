FROM python:3.9

WORKDIR /app

ADD requirements.txt requirements.txt

ADD manager manager

RUN pip install -r requirements.txt

CMD ["python3", "-m", "manager"]
