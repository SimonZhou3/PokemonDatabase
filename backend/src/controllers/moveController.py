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
    def moveFormat(move):
        return { "data": [
            {
                'move_id': move.moveId,
                'name': move.name,
                'type_id': move.typeId,
                'type': move.type,
                'accuracy': move.accuracy,
                'effect_chance': move.effectChance,
                'pp': move.pp,
                'priority': move.priority,
                'power': move.power,
                'damage_class': move.damageClass
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

    @staticmethod
    async def get(move_id):
        print("Get Move Called")
        move = Move(move_id)
        await move.load()
        return MoveController.moveFormat(move)





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