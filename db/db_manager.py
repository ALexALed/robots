import peewee
import datetime


db = peewee.SqliteDatabase('my_database.db')


def init_db():
    db.connect()
    db.create_tables([Route, RouteSteps])



class BaseModel(peewee.Model):
    class Meta:
        database = db


class Route(BaseModel):    
    name = peewee.TextField()
    created_date = peewee.DateTimeField(default=datetime.datetime.now)

    @classmethod
    def save_route(name, steps):
        route = Route.create(
            name=name
        )
        


class RouteSteps(BaseModel):
    route = peewee.ForeignKeyField(Route, backref='steps')
    step_number = peewee.IntegerField()
    x = peewee.IntegerField()
    y = peewee.IntegerField()
