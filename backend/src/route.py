from controllers.locationController import LocationController
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
        print(request.json)
        return await LocationController.create(request.json);
