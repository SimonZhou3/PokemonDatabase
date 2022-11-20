from db import Database
from operator import itemgetter
class Trainer:
    name = None
    trainer_id = None

    @staticmethod
    async def listTrainers():
        SQL = f"SELECT trainer_id,name,gender FROM trainer"
        query = await Database.execute(SQL,None)
        return query

    # Add location to database return id and all information on location
    @staticmethod
    async def create(data):
        name,gender = itemgetter('name','gender')(data)
        SQL = f"INSERT INTO trainer (name,gender) VALUES (%s,%s) RETURNING trainer_id"
        query = await Database.execute(SQL,[name,gender])
        return query[0][0]

    def __init__(self, trainer_id):
        self.trainer_id = trainer_id
        self.name = None
        self.gender = None

    async def load(self):
        SQL = f"SELECT name,gender FROM trainer WHERE trainer_id=(%s)"
        query = await Database.execute(SQL,[self.trainer_id])
        self.name = query[0][0]
        self.gender = query[0][1]

    async def update(self,data):
        self.name = data.get('name') or self.name
        self.gender = data.get('gender') or self.gender
        SQL = f"UPDATE trainer SET name=(%s), gender=(%s) WHERE trainer_id=(%s) RETURNING true"
        await Database.execute(SQL,[self.name,self.gender,self.trainer_id])

    async def delete(self):
        SQL = f"DELETE FROM trainer WHERE trainer_id=(%s) RETURNING true"
        await Database.execute(SQL,[self.trainer_id])

    