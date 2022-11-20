from db import Database
from controllers.moveController import MoveController
from controllers.itemController import ItemController
from models.type import Type
from models.stat import Stat
class Pokemon:

    @staticmethod
    async def listPokemon():
        SQL = "SELECT pokemon_generic_id,name FROM pokemon_generic"
        query = await Database.execute(SQL,None)
        return query

    @staticmethod
    async def getPokemonVersions(generic_id):
        SQL = f"SELECT version_id FROM pokemon_specific WHERE pokemon_generic_id=(%s)"
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
    

    def __init__(self, pokemon_generic_id, version_id):
        self.pokemon_generic_id = pokemon_generic_id
        self.version_id = version_id
        self.initPokemon()


    async def load(self):
        # Get general data
        SQL = (f"SELECT name,height,weight,sprite,pokemon_specific_id,description "
        f"FROM pokemon_generic AS pg,pokemon_specific AS ps "
        f"WHERE pg.pokemon_generic_id =(%s) AND pg.pokemon_generic_id = ps.pokemon_generic_id AND ps.version_id =(%s)")
        print([self.pokemon_generic_id,self.version_id])
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
    

    