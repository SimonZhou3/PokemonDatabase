from db import Database

class Region:
    region_id = None
    name = None
    pokemonCount = None

    @staticmethod
    async def listRegions():
        SQL = (f"SELECT r.region_id, r.name, COUNT(DISTINCT ps.pokemon_generic_id) "
        f"FROM pokemon_specific AS ps, version AS v, version_group AS vg, region AS r "
        f"WHERE vg.version_group_id = v.version_group_id AND v.version_id = ps.version_id AND r.generation_id = vg.generation_id "
        f"GROUP BY r.region_id")
        query = await Database.execute(SQL,None)
        return query

    def __init__(self, region_id):
        self.region_id = region_id

    # Load all region statistic and everything
    async def load(self):
        # SQL = (f"SELECT r.region_id, r.name, COUNT(DISTINCT ps.pokemon_generic_id) "
        # f"FROM pokemon_specific AS ps, version AS v, version_group AS vg, region AS r "
        # f"WHERE vg.version_group_id = v.version_group_id AND v.version_id = ps.version_id AND r.generation_id = vg.generation_id "
        # f"GROUP BY r.region_id")
        # query = await Database.execute(SQL,None)
        # self.name = query[0]
        return None