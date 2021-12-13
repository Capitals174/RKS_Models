# Predict coagulants

Пример файла настроек ***.env***
```
SECRET_KEY=sdkjn4ghjkb4t56lh4566dgdghg9
PYTHONUNBUFFERED=True
DEBUG=False
```

Запуск сервера используя ***docker-compose***: 
```sh
mkdir payload
# скопируйте файлы моделей в папку ./payload

docker-compose up
```

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

## Docker

```sh
cd predict-coagulants
docker build -t predict-coagulants/web:latest .
```


```sh
mkdir payload
# скопируйте файлы моделей в папку ./payload

docker run -p 8000:8000 --rm  \
           -v $(pwd)/payload:/app/payload \
           -e SECRET_KEY='45458sdj@2345kwe' \
           -e DEBUG='False' \
           predict-coagulants/web \
           python3 /app/app.py
```

```sh
127.0.0.1:8000
```

## For production environments...

```sh
cd predict-coagulants
# скопируйте файлы моделей в папку ./app/payload

SECRET_KEY=45458sdjuy2345kwe DEBUG=False python3 ./app/app.py
```
```sh
127.0.0.1:8000
```

## License

MIT
