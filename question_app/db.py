import datetime

import databases
import ormar
import sqlalchemy

from question_app.config import settings

database = databases.Database(settings.db_url)
metadata = sqlalchemy.MetaData()


class BaseMeta(ormar.ModelMeta):
    metadata = metadata
    database = database


class Question(ormar.Model):
    class Meta(BaseMeta):
        tablename = "questions"

    id: int = ormar.Integer(primary_key=True)
    ext_id: int = ormar.Integer(unique=True, nullable=False)
    question_text: str = ormar.String(
        max_length=512, unique=True, nullable=False)
    answer_text: str = ormar.String(max_length=256, nullable=False)
    created_date: datetime.date = ormar.Date(nullable=False)


engine = sqlalchemy.create_engine(settings.db_url)
metadata.create_all(engine)
