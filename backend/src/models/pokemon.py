from db import Database
from controllers.moveController import MoveController
from controllers.itemController import ItemController
from models.type import Type
from models.stat import Stat
from models.area import Area
class Pokemon:

    @staticmethod
    async def listPokemon():
        SQL = "SELECT pokemon_generic_id,name FROM pokemon_generic"
        query = await Database.execute(SQL,None)
        return query

    @staticmethod
    async def getPokemonVersions(generic_id):
        SQL = (f"SELECT version.version_id,name FROM pokemon_specific,version "
         f"WHERE pokemon_generic_id=(%s) AND version.version_id = pokemon_specific.version_id")
        query = await Database.execute(SQL,[generic_id])
        print(query)
        return query

    @staticmethod
    async def getPokemonAreaCountPerRegion(generic_id):
        innerSQL = (f"SELECT ps.pokemon_specific_id, ps.version_id, COUNT(*) AS areaCount "
        f"FROM pokemon_specific as ps "
        f"INNER JOIN pokemon_area as pa ON ps.pokemon_specific_id = pa.pokemon_specific_id "
        f"INNER JOIN pokemon_generic as pg ON pg.pokemon_generic_id = ps.pokemon_generic_id "
        f"WHERE pg.pokemon_generic_id=(%s) GROUP BY ps.pokemon_specific_id, ps.version_id")

        SQL = (f"SELECT r.region_id, r.name, SUM(ps.areaCount) "
        f"FROM ({innerSQL}) AS ps, version AS v, version_group AS vg, region AS r "
        f"WHERE vg.version_group_id = v.version_group_id AND ps.version_id = v.version_id AND r.generation_id = vg.generation_id "
        f"GROUP BY r.region_id")
        query = await Database.execute(SQL,[generic_id])
        print(query)
        return query

    def initPokemon(self):
        self.versionIdList = []
        self.moves = []
        self.items = []
        self.pokemon_specific_id = None
        self.name = None
        self.height = None
        self.sprite = None
        self.stat = None
        self.description = None
        self.type = None
        self.areas = []


    def __init__(self, pokemon_generic_id, version_id):
        self.pokemon_generic_id = int(pokemon_generic_id)
        self.version_id = version_id
        self.initPokemon()


    async def load(self):
        # Get general data
        SQL = (f"SELECT name,height,weight,sprite,pokemon_specific_id,description "
        f"FROM pokemon_generic AS pg INNER JOIN pokemon_specific AS ps ON ps.pokemon_generic_id = pg.pokemon_generic_id  "
        f"WHERE pg.pokemon_generic_id =(%s) AND ps.version_id =(%s)")
        query = await Database.execute(SQL,[self.pokemon_generic_id,self.version_id])
        self.name = query[0][0]
        self.height = query[0][1]
        self.weight = query[0][2]
        self.sprite = query[0][3]
        self.pokemon_specific_id = query[0][4]
        self.description = query[0][5]

        # Get stat
        self.stat = Stat(self.pokemon_generic_id)
        await self.stat.load()
        # Get Type
        self.type = Type(self.pokemon_generic_id)
        await self.type.load()

        # Get moves
        self.moves = await MoveController.list(self.pokemon_specific_id)
        self.moves = self.moves['data']

        # Get items
        self.items = await ItemController.list(self.pokemon_specific_id)
        self.items = self.items['data']

        # Get area
        self.areas = await Area.listPokemonArea(self.pokemon_specific_id)


    async def findPokemonThatAllTrainer(gender):
        if gender is not None:
            SQL = f"SELECT DISTINCT pg.pokemon_generic_id, pg.name, pg.sprite FROM pokemon_specific ps "\
                  f"INNER JOIN pokemon_generic pg ON pg.pokemon_generic_id = ps.pokemon_generic_id "\
                  f"WHERE NOT EXISTS((SELECT t.trainer_id FROM trainer t WHERE t.gender = {gender}) EXCEPT "\
                  f"(SELECT t.trainer_id FROM trained_pokemon tp INNER JOIN trainer t ON t.trainer_id = tp.trainer_id WHERE ps.pokemon_specific_id = tp.pokemon_specific_id)) ORDER BY pg.pokemon_generic_id ASC"
        else:
            SQL = f"SELECT DISTINCT pg.pokemon_generic_id, pg.name, pg.sprite FROM pokemon_specific ps " \
                  f"INNER JOIN pokemon_generic pg ON pg.pokemon_generic_id = ps.pokemon_generic_id " \
                  f"WHERE NOT EXISTS((SELECT t.trainer_id FROM trainer t) EXCEPT " \
                  f"(SELECT t.trainer_id FROM trained_pokemon tp INNER JOIN trainer t ON t.trainer_id = tp.trainer_id WHERE ps.pokemon_specific_id = tp.pokemon_specific_id)) ORDER BY pg.pokemon_generic_id ASC"
        query = await Database.execute(SQL, [])
        return query