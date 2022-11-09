from models.pokemon import pokemon
from operator import itemgetter
from flask import request
class PokemonController:
    @staticmethod
    def listPokemonFormat(locations):
        arr=[]
        for location in locations:
            vals = {}
            vals['pokemon_id']=location[0]
            vals['name']=location[1]
            arr.append(vals)
        return arr

    # @staticmethod
    # def locationFormat(location):
    #     return { "data": [
    #         {
    #             "location_id" : location.location_id,
    #             "name" : location.name,
    #             "version_id": location.version_id
    #         }
    #     ]}


    @staticmethod
    async def list():
        print("List pokemon Called")
        pokemon = await Pokemon.listPokemon()
        result = PokemonController.listPokemonFormat(pokemon)
        return { "data" : result}

    @staticmethod
    async def get(pokemon_id):
        print("Get pokemon Called")
        version_id = request.args.get("version_id")
        pokemon = await Pokemon(pokemon_id,version_id)

        await pokemon.load()
        result = PokemonController.listPokemonFormat(pokemon)
        return { "data" : result}





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