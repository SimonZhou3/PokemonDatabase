from db import Database

class Move:

    def __init__(self, pokemon_specific_id):
        self.pokemon_specific_id = pokemon_specific_id
        self.moves = []


    def formatMoves(self,moves):
        for move in moves:
            vals = {}
            vals['name']=move[0]
            vals['method']=move[1]
            vals['level']=move[2]
            vals['accurancy']=move[3]
            vals['effect_chance']=move[4]
            vals['pp']=move[5]
            vals['priority']=move[6]
            vals['power']=move[7]
            vals['damage_class']=move[8]
            self.moves.append(vals)
        return

    async def load(self):
        SQL = (f"SELECT name,method,level,accuracy,effect_chance,pp,priority,power,damage_class "
        f"FROM pokemon_move AS pm, move "
        f"WHERE pm.pokemon_specific_id =(%s) AND pm.move_id = move.move_id")
        moves = await Database.execute(SQL,[self.pokemon_specific_id])
        self.formatMoves(moves)
        return 
    
    def getMoves(self):
        return self.moves