#change this according to API resource names
api_name = "item"
table = api_name
table_id = table+"_id"

populate_table = True

#index for child id
pokemon_version_specificIndex = 1

def init(cur, pb):
    global populate_table

    #get list of pokemon
    item_list = pb.APIResourceList(api_name)
    item_index = 1
    for item_id in item_list:
        #insert into pokemon table
        item = pb.APIResource(api_name, item_id['name'])
        descriptions = ""
        for desc in item.flavor_text_entries:
            if desc.language.name == "en":
                descriptions = desc.text
        print ("DEBUGGING: ", descriptions)
        print("TUPLE(ITEM): ", item.name, item.cost, item.category.name, descriptions)
        if populate_table:
            cur.execute(
                "INSERT INTO " +  table + " (name, cost, category, description, sprite) VALUES (%s, %s, %s, %s, %s)",
                (item.name, item.cost, item.category.name, descriptions, item.sprites.default))

        #insert into child tables
        item_index+=1
