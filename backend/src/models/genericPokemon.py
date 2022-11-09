from db import Database
class GenericPokemon:

    @staticmethod
    async def listPokemon():
        SQL = "SELECT pokemon_generic_id,name FROM pokemon_generic"
        query = await Database.execute(SQL,None)
        return query


    def __init__(self, pokemon_id, version_id):
        self.pokemon_id = pokemon_id
        self.version_id = version_id
        self.versionIdList = []
        self.name = None
        self.height = None
        self.sprite = None


    async def load(self):
        SQL = f"SELECT * FROM location WHERE location_id=({self.location_id}) LIMIT 1"
        query = await Database.execute(SQL,None)
        self.name = query[0][1]
        self.version_id = query[0][2]