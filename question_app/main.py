import datetime

import asyncio
from http import HTTPStatus
from typing import Union

from fastapi import FastAPI
import httpx

from question_app.db import Question, database
from question_app.exceptions import QuestionException

ENDPOINT = 'https://jservice.io/api/random?count=1'

app = FastAPI(title="Question app")


async def request(client: httpx.AsyncClient) -> dict:
    """Возвращает ответ в формате json от удалённого API вопросов."""
    answer = await client.get(ENDPOINT)
    if answer.status_code != HTTPStatus.OK:
        raise QuestionException("Пришел некорректный ответ от сервера")
    return answer.json()


def is_correct(response_object: dict) -> bool:
    """Проверка объекта вопроса на корректность."""
    if ('id' in response_object
            and 'answer' in response_object
            and 'question' in response_object
            and 'created_at' in response_object
        ) and (
                response_object.get('id')
                and response_object.get('answer')
                and response_object.get('question')
                and response_object.get('created_at')
    ):
        return True
    else:
        return False


@app.post("/")
async def get_question(questions_num: dict) -> Union[Question, None]:
    """Запрашивает с удаленного API заданное в словаре типа
     {questions_num: integer} POST запроса количество вопросов, добавляет все
     полученные вопросы в базу данных, если такой вопрос уже есть - запрашивает
     дополнительный. Возвращает словарь с последним сохраненным вопросом.
    """
    async with httpx.AsyncClient() as client:
        tasks = [
            request(client) for i in range(questions_num.get('questions_num'))]
        result = list(await asyncio.gather(*tasks))
        for question in result:
            this_question = question[0]
            database_exists = await Question.objects.filter(
                question_text=this_question.get('question')).exists()

            if is_correct(this_question) and not database_exists:
                date = this_question.get('created_at')[:10].split('-')
                await Question.objects.create(
                    ext_id=this_question.get('id'),
                    answer_text=this_question.get('answer'),
                    question_text=this_question.get('question'),
                    created_date=datetime.date(
                                year=int(date[0]),
                                month=int(date[1]), day=int(date[2]))
                    )
            else:
                result.append((await asyncio.gather(request(client)))[0])
        return (await Question.objects.all())[-1] or None


@app.on_event("startup")
async def startup():
    if not database.is_connected:
        await database.connect()


@app.on_event("shutdown")
async def shutdown():
    if database.is_connected:
        await database.disconnect()
