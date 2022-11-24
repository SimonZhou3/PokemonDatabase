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
            vals['trainer_id'] = pokemon[0]
            vals['trained_pokemon_id']=pokemon[1]
            vals['pokemon_specific_id']=pokemon[2]
            vals['name'] = pokemon[3]
            vals['nickname']=pokemon[4]
            vals['level']=pokemon[5]
            vals['sprite']=pokemon[6]
            vals['version']=pokemon[7]
            arr.append(vals)
        print(arr)
        return arr


    @staticmethod
    async def listTrainedPokemon(trainer_id):
        SQL = f"SELECT tp.trainer_id, tp.trained_pokemon_id, ps.pokemon_specific_id,pg.name, tp.nickname, tp.level, pg.sprite, v.name " \
              f"FROM trained_pokemon tp INNER JOIN pokemon_specific ps ON ps.pokemon_specific_id = tp.pokemon_specific_id " \
              f"INNER JOIN pokemon_generic pg ON pg.pokemon_generic_id = ps.pokemon_generic_id " \
              f"INNER JOIN version v ON v.version_id = ps.version_id "\
              f"WHERE tp.trainer_id = (%s) "
        query = await Database.execute(SQL,[trainer_id])
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

    async def update(self):
        SQL = f"UPDATE trained_pokemon SET nickname=(%s), level=(%s) WHERE trained_pokemon_id=(%s) RETURNING true"
        await Database.execute(SQL,[self.nickname,self.level,self.trained_pokemon_id])

    async def delete(self):
        SQL = f"DELETE FROM trained_pokemon WHERE trained_pokemon_id=(%s) RETURNING true"
        await Database.execute(SQL,[self.trained_pokemon_id])


    async def getLeaderboard(range, operator):
        SQL = f"SELECT tr.trainer_id, tr.name, COUNT(*) FROM trained_pokemon tp INNER JOIN trainer AS tr ON tp.trainer_id = tr.trainer_id "\
              f"INNER JOIN pokemon_specific AS ps ON ps.pokemon_specific_id = tp.pokemon_specific_id "\
              f"INNER JOIN pokemon_generic pg ON pg.pokemon_generic_id = ps.pokemon_generic_id "\
              f"INNER JOIN pokemon_stat pst ON pst.pokemon_generic_id = pg.pokemon_generic_id "\
              f"GROUP BY tr.trainer_id, tr.name HAVING COUNT(*) {operator} {range} ORDER BY COUNT(*) DESC, tr.name"

        query = await Database.execute(SQL, [])
        return query

