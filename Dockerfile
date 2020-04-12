FROM python:3.8-alpine

LABEL maintainer "Alexandre Corso <alexandre@acorso.fr>"

RUN apk update && apk add g++
RUN pip install gunicorn

COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt

COPY ./app /app
WORKDIR /app

ENV FLASK_ENV production
ENV BIRD_SOCKET /bird.ctl

CMD ["gunicorn", "-b", "0.0.0.0:8179", "wsgi:app", "-w", "4"]%
