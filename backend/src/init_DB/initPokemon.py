from init_DB.initPokemonArea import init as initPokemonAreaTable
from init_DB.initPokemonArea import insert as insertPokemonAreaTable
from init_DB.initPokemonVersion import init as initPokemonVersionTable
from init_DB.initPokemonVersion import insert as insertPokemonVersionTable
from init_DB.initPokemonMove import init as initPokemonMoveTable
from init_DB.initPokemonMove import insert as insertPokemonMoveTable

# TODO -- Add description to table by calling PokemonSpecies. REMEMBER THAT many pokemons can be in different versions.
#change this according to API resource names
api_name = "pokemon"
table = api_name
table_id = table+"_id"
# parent = ""
# fk_id = parent+"_id"

populate_table = True

#index for child id
pokemon_area_id = 1
pokemon_version_id = 1
pokemon_move_id = 1

def init(cur, pb):
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
                description text)
            """)
        print("!!table " + table + " created!!")
        populate_table = True
    #create tables of dependent entities
    initPokemonArea(cur, pb)
    initPokemonVersionTable(cur, pb)
    initPokemonMoveTable(cur, pb)

    #get list of pokemon
    resourceList = pb.APIResourceList(api_name)
    for id, item in enumerate(resourceList):
        #insert into pokemon table
        resource = pb.APIResource(api_name, item['name']);
        print(resource.name)
        if populate_table:
            cur.execute(
                "INSERT INTO " +  table + " (" + table_id + ", name) VALUES (%s, %s)",
                (id + 1 , resource.name,))

        #insert into child tables
        global pokemon_area_id
        for lae in resource.location_area_encounters:
            insertPokemonAreaTable(cur, pb, lae.location_area, lae.version_details, id + 1, pokemon_area_id)
            pokemon_area_id+=1

        global pokemon_version_id
        for game_index in resource.game_indices:
            insertPokemonVersionTable(cur, pb, game_index, id + 1, pokemon_version_id)
            pokemon_version_id+=1

        global pokemon_move_id
        for move in resource.moves:
            insertPokemonMoveTable(cur, pb, move, id + 1, pokemon_move_id)
            pokemon_move_id+=1
