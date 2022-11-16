from controllers.locationController import LocationController
from controllers.pokemonController import PokemonController
from controllers.itemController import ItemController

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
        return await ItemController.list()

    # Item GET
    @app.route("/item/<item_id>", methods=['GET'])
    async def itemGet(item_id):
        return await ItemController.get(item_id)
