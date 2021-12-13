# Predict coagulants

Файл настроек ***.env***
```
SECRET_KEY=sdkjn4ghjkb4t56lh4566dgdghg9
PYTHONUNBUFFERED=True
DEBUG=False
```
Команда запуска: docker-compose up✨
```sh
127.0.0.1:80
```
## Features

- расчет (прогноз) количества коагулянтов

## Tech

Predict-coagulants использует open source projects проекты:

- [python]
- [waitress]
- [Flask]
- [flask-wtf]
- [Flask-bootstrap]
- [numpy]
- [xgboost]
- [sklearn]

## Installation

Predict-coagulants тестировался на **python>=3.6**
Для ручной сборки установите зависимости из **requirements.txt**

```sh
cd predict-coagulants
pip install -r requirements.txt
```

## For production environments...

```sh
cd predict-coagulants
SECRET_KEY=45458sdjuy2345kwe DEBUG=False python3 ./app/app.py
```
```sh
127.0.0.1:8000
```
## Docker

```sh
cd predict-coagulants
docker build -t predict-coagulants .
```

```sh
docker run -d -p 8000:8080 \
-e SECRET_KEY='45458sdj@2345kwe' \
-e DEBUG='False' \
--restart=always predict-coagulants
```

```sh
127.0.0.1:8000
```

## License

MIT
