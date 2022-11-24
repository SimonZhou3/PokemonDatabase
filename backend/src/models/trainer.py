from db import Database
from operator import itemgetter
from models.trainedPokemon import TrainedPokemon
class Trainer:
    name = None
    trainer_id = None
    pokemon = []

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
        print("Finish loading trainer data")
        self.pokemon = await TrainedPokemon.listTrainedPokemon(self.trainer_id)
        print("Finish loading trained pokemons")



    async def update(self,data):
        self.name = data.get('name') or self.name
        self.gender = data.get('gender') or self.gender
        SQL = f"UPDATE trainer SET name=(%s), gender=(%s) WHERE trainer_id=(%s) RETURNING true"
        await Database.execute(SQL,[self.name,self.gender,self.trainer_id])

    async def delete(self):
        SQL = f"DELETE FROM trainer WHERE trainer_id=(%s) RETURNING true"
        await Database.execute(SQL,[self.trainer_id])

    async def getPokemonOwnedCount(self):
        SQL = (f"SELECT tp.pokemon_specific_id, pg.name, COUNT(tp.pokemon_specific_id) FROM trained_pokemon tp "
        f"INNER JOIN trainer AS tr ON tp.trainer_id = tr.trainer_id "
        f"INNER JOIN pokemon_specific AS ps ON tp.pokemon_specific_id = ps.pokemon_specific_id "
        f"INNER JOIN pokemon_generic AS pg ON pg.pokemon_generic_id = ps.pokemon_generic_id "
        f"WHERE tr.trainer_id = (%s) GROUP BY tp.pokemon_specific_id, pg.name")
        query = await Database.execute(SQL, [self.trainer_id])
        return query
