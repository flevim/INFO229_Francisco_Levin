FROM python:3.6.3

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

ENV PYTHONUNBUFFERED=1
ENV WEATHER_API_KEY="8b1713b635fa5884b391b173b33386c1"

WORKDIR /bot_weather_search

COPY ./bot_weather_search.py /bot_weather_search.py

CMD [ "python", "/bot_weather_search.py" ]
