from db import Database
from operator import itemgetter
class Trainer:
    name = None
    trainer_id = None

    @staticmethod
    async def listTrainers():
        SQL = "SELECT trainer_id,name FROM trainer"
        query = await Database.execute(SQL,None)
        return query

    # Add location to database return id and all information on location
    @staticmethod
    async def create(name):
        SQL = f"INSERT INTO trainer (name) VALUES (%s) RETURNING trainer_id"
        query = await Database.execute(SQL,[name])
        return query[0][0]

    def __init__(self, trainer_id):
        self.trainer_id = trainer_id
        self.name = None

    async def load(self):
        SQL = f"SELECT name FROM trainer WHERE trainer_id=(%s)"
        query = await Database.execute(SQL,[self.trainer_id])
        self.name = query[0][0]

    async def update(self,data):
        name = itemgetter('name')(data)
        self.name = name
        SQL = f"UPDATE trainer SET name=(%s) WHERE trainer_id=(%s) RETURNING true"
        await Database.execute(SQL,[self.name,self.trainer_id])

    async def delete(self):
        SQL = f"DELETE FROM trainer WHERE trainer_id=(%s) RETURNING true"
        await Database.execute(SQL,[self.trainer_id])

    