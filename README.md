# Service for obtaining unique questions for quizzes

question_app

## Description

In the POST request to the API address in the request body, you must specify the number
of questions requested from an external server. The required number of unique
questions will be saved in the database. The answer to the POST request is the last
Question object saved in the database.

## Technologies

    asyncpg==0.25.0
    fastapi==0.75.2
    ormar==0.11.0
    psycopg2-binary==2.9.3
    pydantic==1.9.0
    SQLAlchemy==1.4.31
    uvicorn==0.17.6
    httpx~=0.22.0
    databases~=0.5.5

## Dev-mode run

Clone files from the repository to register in the console:

    git clone git@gitlab.com:Pavelkalininn/test_task.git


### For centralized project launch via docker-compose:
Create images and launch new containers in the directory with the docker-compose file.yml:
If you don't want an open docker-compose hanging in the console,
run it as a process, with the -d option.

    docker-compose up -d --build

To install containers, run:

    docker-compose down 

After launching all containers, you can read the API documentation at:

    http://127.0.0.1:8008/docs   (SWAGGER)
    http://127.0.0.1:8008/redoc/  (REDOC)

## Address for POST API requests:

    http://127.0.0.1:8008/

## Example of a POST request to the address http://127.0.0.1:8008/:
In the request body:

    {
        "questions_num": 2
    }

## Answer:
    
    {
        "id": 2,
        "ext_id": 6933,
        "question_text": 
            "Snakes used in these acts sway in response to the musician's"
            "movements; they can't really hear the music",
        "answer_text": "Snake Charmer",
        "created_date": "2014-02-11"
    }

### All the Question objects created via the API are saved in the PostgreSQL database.


Author __Pavel Kalinin__ pavelkalininn@gmail.com
