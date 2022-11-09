# TODO -- Add description to table by calling PokemonSpecies. REMEMBER THAT many pokemons can be in different versions.
#change this according to API resource names
api_name = "item"
table = api_name
table_id = table+"_id"
# parent = ""
# fk_id = parent+"_id"

populate_table = True

#index for child id
pokemon_version_specificIndex = 1

def init(cur, pb):
    global populate_table
    #if the table exist then skip entirely
    cur.execute("SELECT EXISTS(SELECT * FROM information_schema.tables WHERE table_name='"+table+"')")
    if bool(cur.fetchone()[0]):
        print("**table " + table + " exists already**")
        populate_table = False
    else :
        # Execute a command: this creates a new table
        cur.execute("""
            CREATE TABLE """ + table + """ (
                """+ table_id + """  integer PRIMARY KEY,
                name text,
                cost integer,
                category text,
                description text,
                sprite text
                )
            """)
        print("!!table " + table + " created!!")
        populate_table = True
    #create tables of dependent entities
    # initPokemonSpecificTable(cur, pb)

    #get list of pokemon
    item_list = pb.APIResourceList(api_name)
    item_index = 1
    for item_id in item_list:
        #insert into pokemon table
        item = pb.APIResource(api_name, item_id['name']);
        descriptions = []
        for desc in item.flavor_text_entries:
            if desc.language.name == "en":
                descriptions.append(desc.text)
        print("TUPLE(ITEM): ", item.name, item.cost, item.category.name, descriptions[-1])
        if populate_table:
            cur.execute(
                "INSERT INTO " +  table + " (" + table_id + ", name, cost, category, description, sprite) VALUES (%s, %s, %s, %s, %s, %s)",
                (item_index , item.name, item.cost, item.category.name, item.flavor_text_entries[0].text, item.sprites.default))

        #insert into child tables
        item_index+=1
