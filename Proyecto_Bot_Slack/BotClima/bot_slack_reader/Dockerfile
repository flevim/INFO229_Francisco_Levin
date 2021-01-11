FROM python:3.6.3

ENV SLACK_TOKEN=
ENV SLACK_SIGNING_SECRET=

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

ENV PYTHONUNBUFFERED=1

WORKDIR /nestor_slack_reader

COPY ./bot_slack_reader.py /bot_slack_reader.py

CMD [ "python", "/bot_slack_reader.py" ]
