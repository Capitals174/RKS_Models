FROM python:3.8-buster
ENV FLASK_ENV=production \
    PYTHONUNBUFFERED=True
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY ./app /app
COPY ./payload /app/payload

