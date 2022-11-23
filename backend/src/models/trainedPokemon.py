from db import Database
from operator import itemgetter

class TrainedPokemon:
    trained_pokemon_id = None
    pokemon_specific_id = None
    trainer_id = None
    nickname = None
    level = None

    @staticmethod
    def listTrainedPokemonFormat(pokemons):
        arr=[]
        for pokemon in pokemons:
            vals = {}
            vals['trained_pokemon_id']=pokemon[0]
            vals['pokemon_specific_id']=pokemon[1]
            vals['trainer_id']=pokemon[2]
            vals['nickname']=pokemon[3]
            vals['level']=pokemon[4]
            arr.append(vals)
        print(arr)
        return arr


    @staticmethod
    async def listTrainedPokemon(trainer_id):
        SQL = f"SELECT * FROM trained_pokemon WHERE trainer_id = (%s)"
        query = await Database.execute(SQL,[trainer_id])
        print(query)
        return TrainedPokemon.listTrainedPokemonFormat(query)

    @staticmethod
    async def create(trainer_id,data):
        pokemon_specific_id,nickname,level = itemgetter('pokemon_specific_id','nickname','level')(data)
        SQL = (f"INSERT INTO trained_pokemon (pokemon_specific_id,trainer_id,nickname,level) "
        f"VALUES (%s,%s,%s,%s) RETURNING trained_pokemon_id")
        query = await Database.execute(SQL,[pokemon_specific_id,trainer_id,nickname,level])
        return query[0][0]


    def __init__(self, trained_pokemon_id):
        self.trained_pokemon_id = trained_pokemon_id
    

    async def load(self):
        SQL = f"SELECT pokemon_specific_id,trainer_id,nickname,level FROM trained_pokemon WHERE trained_pokemon_id=(%s)"
        query = await Database.execute(SQL,[self.trained_pokemon_id])
        self.pokemon_specific_id = query[0][0]
        self.trainer_id = query[0][1]
        self.nickname = query[0][2]
        self.level = query[0][3]
        print("Finish loading trained pokemon data")
        return 

    async def delete(self):
        SQL = f"DELETE FROM trained_pokemon WHERE trained_pokemon_id=(%s) RETURNING true"
        await Database.execute(SQL,[self.trained_pokemon_id])
