FROM python:3.9

WORKDIR /app

ADD requirements.txt requirements.txt

ADD main.py main.py

RUN pip install -r requirements.txt

ADD app app

CMD ["python", "main.py"]
