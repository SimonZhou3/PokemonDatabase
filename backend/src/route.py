from entities.pokemon import Pokemon
def routes(app):
    @app.route("/")
    def hello_world():
        return "<p>Welcome to the backend pokemon server</p>" 


    # Pokemon
    @app.route("/pokemon", methods=['GET'])
    def run():
        return Pokemon.listPokemon()


    # Location
    @app.route("/location", methods=['GET'])
    def run():
        return Pokemon.listPokemon()
