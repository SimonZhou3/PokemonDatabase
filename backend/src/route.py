from controllers.locationController import LocationController
from controllers.pokemonController import PokemonController
from controllers.itemController import ItemController
from controllers.moveController import MoveController
from controllers.trainerController import TrainerController
from controllers.regionController import RegionController

from flask import request


def routes(app):
    @app.route("/")
    def home():
        return "<p>Welcome to the backend pokemon server</p>"

    # Location LIST
    @app.route("/location", methods=['GET'])
    async def locationList():
        return await LocationController.list();

    # Location POST
    @app.route("/location", methods=['POST'])
    async def locationCreate():
        return await LocationController.create(request.json);

    # Pokemon LIST
    @app.route("/pokemon", methods=['GET'])
    async def pokemonList():
        return await PokemonController.list();

    # Pokemon GET
    @app.route("/pokemon/<pokemon_id>", methods=['GET'])
    async def pokemonGet(pokemon_id):
        return await PokemonController.get(pokemon_id)

    # Item LIST
    @app.route("/item", methods=['GET'])
    async def itemList():
        pokemon_specific_id = request.args.get("pokemon_specific_id")
        return await ItemController.list(pokemon_specific_id)

    # Item GET
    @app.route("/item/<item_id>", methods=['GET'])
    async def itemGet(item_id):
        return await ItemController.get(item_id)

    # Move LIST
    @app.route("/move", methods=['GET'])
    async def moveList():
        pokemon_specific_id = request.args.get("pokemon_specific_id")
        return await MoveController.list(pokemon_specific_id)

    # Move GET
    @app.route("/move/<move_id>", methods=['GET'])
    async def moveGet(move_id):
        return await MoveController.get(move_id)


    #Trainer LIST
    @app.route("/trainer", methods=['GET'])
    async def trainerList():
        return await TrainerController.list()

    #Trainer CREATE
    @app.route("/trainer/<trainer_id>", methods=['GET'])
    async def trainerGet(trainer_id):
        return await TrainerController.get(trainer_id)

    #Trainer CREATE
    @app.route("/trainer", methods=['POST'])
    async def trainerCreate():
        return await TrainerController.create(request.json)

    #Trainer UPDATE
    @app.route("/trainer/<trainer_id>", methods=['PUT'])
    async def trainerUpdate(trainer_id):
        return await TrainerController.update(trainer_id,request.json)

    #Trainer Add pokemon
    @app.route("/trainer/<trainer_id>/pokemon", methods=['POST'])
    async def trainerAddPokemon(trainer_id):
        return await TrainerController.addPokemon(trainer_id,request.json)

    #Trainer Update pokemon
    @app.route("/trainer/<trainer_id>/pokemon/<trained_pokemon_id>", methods=['PUT'])
    async def trainerUpdatePokemon(trainer_id,trained_pokemon_id):
        return await TrainerController.updatePokemon(trainer_id,trained_pokemon_id,request.json)

    #Trainer Delete pokemon
    @app.route("/trainer/<trainer_id>/pokemon/<trained_pokemon_id>", methods=['DELETE'])
    async def trainerRemovePokemon(trainer_id,trained_pokemon_id):
        return await TrainerController.removePokemon(trained_pokemon_id)

    #Trainer Delete
    @app.route("/trainer/<trainer_id>", methods=['DELETE'])
    async def trainerDelete(trainer_id):
        return await TrainerController.delete(trainer_id)

    #Region LIST
    @app.route("/region", methods=['GET'])
    async def regionList():
        return await RegionController.list()

    #Region GET // CONTAINS GROUP SQL
    @app.route("/region/<region_id>", methods=['GET'])
    async def regionGet(region_id):
        return await RegionController.get(region_id)

    #Pokemon statistics MAY REMOVE
    @app.route("/stats/region/<region_id>/pokemon_count", methods=['GET'])
    async def regionPokemonCount(region_id):
        return None

    # Find the count of each trained pokemon by trainer.
    # Note -- operator takes: >, <, >=, <=, <>
    @app.route("/trainer/leaderboard", methods=['GET'])
    async def getLeaderboard():
        filter_range = request.args.get('range')
        operator = request.args.get('operator')
        return await TrainerController.getHighestStats(filter_range,operator)


    @app.route("/trainer/<trainer_id>/pokemonCount", methods=['GET'])
    async def getTrainerPokemonCount(trainer_id):
        return await TrainerController.getPokemonCount(trainer_id)

    # Using division this route finds a pokemon that all trainers has. User can specify Gender or not.
    @app.route("/trainer/all")
    async def getAllTrainerByFilters():
        gender = request.args.get('gender')
        print(gender)
        return await PokemonController.findPokemonThatAllTrainer(gender)