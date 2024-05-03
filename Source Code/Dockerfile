FROM python:3.7.17-alpine3.18



WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql \
    && apk add postgresql-dev \
    && pip install psycopg2 \
    && apk add jpeg-dev zlib-dev libjpeg \
    && pip install Pillow \
    && apk del build-deps

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /usr/src/app/



CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

EXPOSE 8000