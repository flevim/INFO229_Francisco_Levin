FROM python:3.6.3

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

ENV PYTHONUNBUFFERED=1

WORKDIR /consumer

COPY ./consumer.py /consumer.py

CMD [ "python", "/consumer.py" ]
