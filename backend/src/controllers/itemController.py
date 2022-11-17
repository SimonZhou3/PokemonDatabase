from models.item import Item
from operator import itemgetter
from flask import request
class ItemController:
    @staticmethod
    def listItemFormat(items):
        arr=[]
        for item in items:
            vals = {}
            vals['item_id']=item[0]
            vals['name']=item[1]
            try:
                vals['rarity'] = item[2]
            except:
                None
            arr.append(vals)
        return arr

    @staticmethod
    def itemFormat(item):
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
        print("List item Called")
        items = None
        if (pokemon_specific_id):
            items = await Item.listPokemonItem(pokemon_specific_id)  
        else:
            items = await Item.listItem()
        result = ItemController.listItemFormat(items)
        return { "data" : result}

    @staticmethod
    async def get(item_id):
        print("Get Item Called")
        item = Item(item_id)
        await item.load()
        return ItemController.itemFormat(item)





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