from models.move import Move
from operator import itemgetter
from flask import request
class MoveController:
    @staticmethod
    def listMoveFormat(items):
        arr=[]
        for item in items:
            vals = {}
            vals['move_id']=item[0]
            vals['name']=item[1]
            arr.append(vals)
        return arr

    @staticmethod
    def moveFormat(item):
        return { "data": [
            {
                'item_id': item.item_id,
                'name': item.name,
                'cost': item.cost,
                'category': item.category,
                'description': item.description,
                'sprite': item.sprite
            }]}


    @staticmethod
    async def list(pokemon_specific_id):
        print("List moves Called")
        moves = None
        if (pokemon_specific_id):
            moves = await Move.listPokemonMoves(pokemon_specific_id)  
        else:
            moves = await Move.listMoves()  
        result = MoveController.listMoveFormat(moves)
        return { "data" : result}

    # @staticmethod
    # async def get(item_id):
    #     print("Get Item Called")
    #     item = Item(item_id)
    #     await item.load()
    #     return ItemController.listMoveFormat(item)





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