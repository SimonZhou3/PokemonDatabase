from models.pokemon import Pokemon
from operator import itemgetter
from flask import request
class PokemonController:
    @staticmethod
    def listPokemonFormat(pokemons):
        arr=[]
        for pokemon in pokemons:
            vals = {}
            vals['pokemon_id']=pokemon[0]
            vals['name']=pokemon[1]
            arr.append(vals)
        return arr

    @staticmethod
    def pokemonFormat(pokemon):
        return { "data": [
            {
                "pokemon_specific_id": pokemon.pokemon_specific_id,
                "pokemon_version_id": pokemon.version_id,
                "name" : pokemon.name,
                "height" : pokemon.height,
                "sprite" : pokemon.sprite,
                "description": pokemon.description,
                "stat": pokemon.stat.getStats(),
                "type": pokemon.type.getTypes(),
                "moves": pokemon.moves.getMoves()
            }]}


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
        result = None
        if (not version_id):
            versionIdList = await Pokemon.getPokemonVersions(pokemon_id)
            pokemon = Pokemon(pokemon_id,versionIdList[0][0])
            await pokemon.load()
            result = PokemonController.pokemonFormat(pokemon)
        else:
            pokemon = Pokemon(pokemon_id,version_id)
            await pokemon.load()
            result = PokemonController.pokemonFormat(pokemon)
        return result





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