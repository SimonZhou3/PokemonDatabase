from models.region import Region
from operator import itemgetter

class RegionController:
    @staticmethod
    def listRegionFormat(regions):
        arr=[]
        for region in regions:
            vals = {}
            vals['region_id']=region[0]
            vals['name']=region[1]
            vals['pokemon_count']=region[2]
            arr.append(vals)
        return arr


    @staticmethod
    async def list():
        regions = await Region.listRegions()
        result = RegionController.listRegionFormat(regions)
        return { "data" : result}

    @staticmethod
    async def get(region_id):
        region = Region(region_id)
        await region.load()
        return None

    # @staticmethod
    # async def create(data):
    #     name,version_id = itemgetter('name', 'version_id')(data)
    #     location_id = await Location.addLocation(name,version_id)
    #     location = Location(location_id)
    #     await location.load()
    #     return LocationController.locationFormat(location)

    # @staticmethod
    # async def update(data):
    #     location = Location(location_id)
    #     return { "data" : None}

    # @staticmethod
    # async def delete(data):
    #     location = Location()
    #     return { "data" : None}