from controllers.locationController import LocationController
from controllers.pokemonController import PokemonController


from flask import request


def routes(app):
    @app.route("/")
    def home():
        return "<p>Welcome to the backend pokemon server</p>" 
    
    # Location
    @app.route("/location", methods=['GET'])
    async def locationList():
        return await LocationController.list();
    
    # Location
    @app.route("/location", methods=['POST'])
    async def locationCreate():
        return await LocationController.create(request.json);

    # Pokemon
    @app.route("/pokemon", methods=['GET'])
    async def pokemonList():
        return await PokemonController.list();

    # Pokemon
    @app.route("/pokemon/<pokemon_id>", methods=['GET'])
    async def pokemonGet(pokemon_id):
        return await PokemonController.get(pokemon_id)
