from db import Database

class Move:

    @staticmethod
    async def listPokemonMoves(pokemon_specific_id):
        SQL = (f"SELECT move.move_id, name "
        f"FROM pokemon_move AS pm, move "
        f"WHERE pm.pokemon_specific_id =(%s) AND pm.move_id = move.move_id")
        query = await Database.execute(SQL,[pokemon_specific_id])
        return query

    @staticmethod
    async def listMoves():
        SQL = f"SELECT move_id,name FROM move"
        query = await Database.execute(SQL,None)
        return query


    def __init__(self, move_id):
        self.moveId = move_id
        self.typeId = None,
        self.name = None,
        self.accuracy = None,
        self.effectChance = None,
        self.pp = None,
        self.priority = None,
        self.power = None,
        self.damageClass = None

    async def load(self):
        SQL = (f"SELECT * "
        f"FROM move,type "
        f"WHERE move.move_id=(%s) AND type.type_id = move.type_id LIMIT 1")
        move = await Database.execute(SQL,[self.moveId])
        print(move)
        self.name = move[0][2]
        self.accuracy = move[0][3]
        self.effectChance = move[0][4]
        self.pp = move[0][5]
        self.priority = move[0][6]
        self.power = move[0][7]
        self.damageClass = move[0][8]
        self.typeId = move[0][9]
        self.type = move[0][10]
        return 
    