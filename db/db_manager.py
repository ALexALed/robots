import os
import peewee
import datetime

TEST_RUN = False


def get_db_name():
    return 'database.db' if not TEST_RUN else 'test_database.db'


def init_db():
    db = peewee.SqliteDatabase(get_db_name())
    db.connect()
    db.create_tables([RouteModel, RouteStepsModel])


def remove_db():
    os.remove(get_db_name())


class BaseModel(peewee.Model):
    class Meta:
        database = peewee.SqliteDatabase(get_db_name())


class RouteModel(BaseModel):
    created_date = peewee.DateTimeField(default=datetime.datetime.now)

    @classmethod
    def save_route(cls):
        return RouteModel.create()

    def save_step(self, x, y):
        RouteStepsModel.create(
            route=self,
            x=x,
            y=y,
        )


class RouteStepsModel(BaseModel):
    route = peewee.ForeignKeyField(RouteModel, backref='steps')
    x = peewee.IntegerField()
    y = peewee.IntegerField()
