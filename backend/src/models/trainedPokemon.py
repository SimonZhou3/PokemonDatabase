from db import Database

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

    def __init__(self, trainer_id):
        self.trainer_id = trainer_id