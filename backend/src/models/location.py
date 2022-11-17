from db import Database

class Location:
    name = None
    version_id = None

    @staticmethod
    async def listLocations():
        SQL = "SELECT location_id,name FROM location"
        query = await Database.execute(SQL,None)
        return query

    # Add location to database return id and all information on location
    @staticmethod
    async def addLocation(name,version_id):
        SQL = f"INSERT INTO location (name,region_id) VALUES (%s, %s) RETURNING location_id"
        query = await Database.execute(SQL,(name,version_id))
        return query[0][0]

    def __init__(self, location_id):
        self.location_id = location_id
        self.name = None
        self.location = None

    async def load(self):
        SQL = f"SELECT * FROM location WHERE location_id=({self.location_id})"
        query = await Database.execute(SQL,None)
        self.name = query[0][1]
        self.version_id = query[0][2]

    