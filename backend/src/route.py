from controllers.locationController import LocationController
from controllers.pokemonController import PokemonController
from controllers.itemController import ItemController
from controllers.moveController import MoveController
from controllers.trainerController import TrainerController

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

    #Trainer LIST
    @app.route("/trainer", methods=['POST'])
    async def trainerCreate():
        return await TrainerController.create(request.json)