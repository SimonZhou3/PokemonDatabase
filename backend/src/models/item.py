from db import Database

class Item:

    @staticmethod
    async def listItem():
        SQL = "SELECT item_id,name FROM item"
        query = await Database.execute(SQL,None)
        return query

    @staticmethod
    async def listPokemonItem(pokemon_specific_id):
        SQL = (f"SELECT item.item_id,name,rarity FROM item,pokemon_item as pi "
        f"WHERE pi.pokemon_specific_id = (%s) AND item.item_id = pi.item_id")
        query = await Database.execute(SQL,[pokemon_specific_id])
        print(query)
        return query

    def itemFormat(self,item):
        self.name = item[0]

    def __init__(self,item_id):
        self.item_id = item_id
        self.name = None
        self.cost = None
        self.category = None
        self.description = None
        self.sprite = None
        return

    async def load(self):
        SQL = (f"SELECT name,cost,category,description,sprite FROM item WHERE item_id=(%s) LIMIT 1")
        query = await Database.execute(SQL,[self.item_id])
        self.name = query[0][0]
        self.cost = query[0][1]
        self.category = query[0][2]
        self.description = query[0][3]
        self.sprite = query[0][4]
        return
    