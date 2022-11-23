from db import Database

class Area:

    @staticmethod
    def listPokemonAreaFormat(areas):
        arr=[]
        for area in areas:
            vals = {}
            vals['area_id']=area[0]
            vals['area_name']=area[1]
            vals['location_id'] = area[2]
            vals['location_name'] = area[3]
            arr.append(vals)
        return arr

    @staticmethod
    async def listPokemonArea(pokemon_specific_id):
        SQL = (f"SELECT area.area_id, area.name, area.location_id, location.name "
        f"FROM pokemon_area AS pa, area, location "
        f"WHERE pa.pokemon_specific_id =(%s) AND pa.area_id = area.area_id AND area.location_id = location.location_id")
        query = await Database.execute(SQL,[pokemon_specific_id])
        return Area.listPokemonAreaFormat(query)

    def __init__(self, area_id):
        self.area_id = area_id

    async def load(self):
        return 
    