from db import Database

class Type:

    def __init__(self, pokemon_generic_id):
        self.pokemon_generic_id = pokemon_generic_id
        self.types = []


    def formatTypes(self,types):
        for type in types:
            vals = {}
            vals['type']=type[0]
            vals['slot']=type[1]
            self.types.append(vals)
            return

    async def load(self):
        SQL = (f"SELECT name,slot "
        f"FROM type, pokemon_type "
        f"WHERE pokemon_type.pokemon_generic_id = (%s) AND pokemon_type.type_id = type.type_id")
        types = await Database.execute(SQL,[self.pokemon_generic_id])
        self.formatTypes(types)
        return 
    
    def getTypes(self):
        return self.types