# Сервис получения уникальных вопросов для викторин

question_app

## Описание

В POST запросе на адрес API в теле запроса необходимо указать количество
вопросов, запрашиваемое с внешнего сервера. Необходимое количество уникальных
вопросов сохранится в базе данных. Ответом на POST запрос служит последний
сохраненный в БД объект Question.

## Технологии

    asyncpg==0.25.0
    fastapi==0.75.2
    ormar==0.11.0
    psycopg2-binary==2.9.3
    pydantic==1.9.0
    SQLAlchemy==1.4.31
    uvicorn==0.17.6
    httpx~=0.22.0
    databases~=0.5.5

## Запуск проекта в dev-режиме

Клонирование файлов из репозитория прописать в консоли:

    git clone git@gitlab.com:Pavelkalininn/test_task.git


### Для централизованного запуска проекта через docker-compose:
Создайте образы и запустите новые контейнеры в директории с файлом docker-compose.yml:
Если вы не хотите, чтобы в консоли висел открытый docker-compose, 
запускайте его как процесс, с опцией -d.

    docker-compose up -d --build

Для остановки контейнеров запустите:

    docker-compose down 

После запуска всех контейнеров можно ознакомится документацией на API по адресу:

    http://127.0.0.1:8008/docs   (SWAGGER)
    http://127.0.0.1:8008/redoc/  (REDOC)

## Адрес для POST запросов к API:

    http://127.0.0.1:8008/

## Пример POST запроса на адрес http://127.0.0.1:8008/:
В теле запроса:

    {
        "questions_num": 2
    }

## Пример ответа:
    
    {
        "id": 2,
        "ext_id": 6933,
        "question_text": 
            "Snakes used in these acts sway in response to the musician's"
            "movements; they can't really hear the music",
        "answer_text": "Snake Charmer",
        "created_date": "2014-02-11"
    }

### Все созданные через API объекты Question сохраняются в БД PostgreSQL. 


Автор __Паша Калинин__ pavelkalininn@gmail.com
