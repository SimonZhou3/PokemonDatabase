from db import Database

class Stat:

    def __init__(self, pokemon_generic_id):
        self.pokemon_generic_id = pokemon_generic_id
        self.hp = None
        self.attack = None
        self.defence = None
        self.specialAttack = None
        self.specialDefence = None
        self.speed = None


    def formatStats(self,stats):
        self.hp = stats[0]
        self.attack = stats[1]
        self.defence = stats[2]
        self.specialAttack = stats[3]
        self.specialDefence = stats[4]
        self.speed = stats[5]


    async def load(self):
        SQL = (f"SELECT hp,attack,defence,special_attack,special_defence,speed "
        f"FROM pokemon_stat "
        f"WHERE pokemon_stat.pokemon_generic_id= (%s) LIMIT 1")
        stats = await Database.execute(SQL,[self.pokemon_generic_id])
        self.formatStats(stats[0])
        return 
    
    def getStats(self):
        return {
            "hp": self.hp,
            "attack": self.attack, 
            "defence": self.defence, 
            "specialAttack": self.specialAttack, 
            "specialDefence": self.specialDefence,
            "speed": self.speed, 
        }
            