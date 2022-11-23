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

    def versionIdFormat(versionIdList):
        arr = []
        for version in versionIdList:
            vals = {}
            vals['version_id']=version[0]
            vals['name']=version[1]
            arr.append(vals)
        return arr      
        
    @staticmethod
    def pokemonFormat(pokemon,versionIdList):
        return { "data": [
            {   "pokemon_generic_id": pokemon.pokemon_generic_id,
                "pokemon_specific_id": pokemon.pokemon_specific_id,
                "pokemon_version_id": pokemon.version_id,
                "version_list": PokemonController.versionIdFormat(versionIdList),
                "name" : pokemon.name,
                "height" : pokemon.height,
                "sprite" : pokemon.sprite,
                "description": pokemon.description,
                "stat": pokemon.stat.getStats(),
                "type": pokemon.type.getTypes(),
                "moves": pokemon.moves,
                "items": pokemon.items,
                "areas": pokemon.areas
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
        versionIdList = await Pokemon.getPokemonVersions(pokemon_id)
        if (not version_id):
            pokemon = Pokemon(pokemon_id,versionIdList[0][0])
            await pokemon.load()
            result = PokemonController.pokemonFormat(pokemon,versionIdList)
        else:
            pokemon = Pokemon(pokemon_id,version_id)
            await pokemon.load()
            result = PokemonController.pokemonFormat(pokemon,versionIdList)
        return result



    @staticmethod
    async def findPokemonThatAllTrainer(gender):
        result = await Pokemon.findPokemonThatAllTrainer(gender);
        jsonArray = []
        for pokemon_data in result:
            jsonObject = {
                "pokemon_id": pokemon_data[0],
                "name": pokemon_data[1]
            }
            jsonArray.append(jsonObject)
        return  {
        "data": jsonArray
        }



    # @staticmethod
    # async def create(data):
    #     try:
    #         name,version_id = itemgetter('name', 'version_id')(data)
    #         location_id = await Pokemon.create(name,version_id)
    #     except:
    #         print("An exception occurred")
    
  

    # @staticmethod
    # async def update(data):
    #     location = Location(location_id)
    #     return { "data" : None}

    # @staticmethod
    # async def delete(data):
    #     location = Location()
    #     return { "data" : None}