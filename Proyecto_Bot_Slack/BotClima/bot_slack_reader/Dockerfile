FROM python:3.6.3

ENV SLACK_TOKEN=xoxb-1497700884193-1470344062183-SDNBHFEXqx0vcbLXRKYSHA0f
ENV SLACK_SIGNING_SECRET=461310e0feb09b6837e01657332feb89

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

ENV PYTHONUNBUFFERED=1

WORKDIR /nestor_slack_reader

COPY ./bot_slack_reader.py /bot_slack_reader.py

CMD [ "python", "/bot_slack_reader.py" ]
