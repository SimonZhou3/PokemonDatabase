from models.location import Location
from operator import itemgetter

class LocationController:
    @staticmethod
    def listLocationFormat(locations):
        arr=[]
        for location in locations:
            vals = {}
            vals['location_id']=location[0]
            vals['name']=location[1]
            arr.append(vals)
        return arr

    @staticmethod
    def locationFormat(location):
        return { "data": [
            {
                "location_id" : location.location_id,
                "name" : location.name,
                "version_id": location.version_id
            }
        ]}


    @staticmethod
    async def list():
        location = await Location.listLocations()
        result = LocationController.listLocationFormat(location)
        return { "data" : result}

    @staticmethod
    async def create(data):
        name,version_id = itemgetter('name', 'version_id')(data)
        location_id = await Location.addLocation(name,version_id)
        location = Location(location_id)
        await location.load()
        return LocationController.locationFormat(location)

    @staticmethod
    async def update(data):
        location = Location()
        return { "data" : None}

    @staticmethod
    async def delete(data):
        location = Location()
        return { "data" : None}