from init_DB.initPokemonSpecific import init as initPokemonSpecificTable
from init_DB.initPokemonSpecific import insert as insertPokemonSpecificTable
from init_DB.initPokemonMove import init as initPokemonMoveTable
from init_DB.initPokemonMove import insert as insertPokemonMoveTable
from init_DB.initPokemonArea import init as initPokemonAreaTable
from init_DB.initPokemonArea import insert as insertPokemonAreaTable
from init_DB.initPokemonType import init as initPokemonTypeTable
from init_DB.initPokemonType import insert as insertPokemonTypeTable
# TODO -- Add description to table by calling PokemonSpecies. REMEMBER THAT many pokemons can be in different versions.
#change this according to API resource names
api_name = "pokemon"
table = "pokemon_generic"
table_id = table+"_id"
# parent = ""
# fk_id = parent+"_id"

populate_table = True

#index for child id
pokemon_version_specificIndex = 1
pokemon_moveIndex = 1
pokemon_areaIndex = 1
pokemon_typeIndex = 1

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
                height integer,
                weight integer,
                sprite text
                )
            """)
        print("!!table " + table + " created!!")
        populate_table = True
    #create tables of dependent entities
    initPokemonSpecificTable(cur, pb)
    initPokemonMoveTable(cur,pb)
    initPokemonAreaTable(cur, pb)
    initPokemonTypeTable(cur,pb)

    #get list of pokemon
    pokemonList = pb.APIResourceList(api_name)
    pokemon_index = 1
    for poke_id in pokemonList:
        #insert into pokemon table
        pokemon = pb.APIResource(api_name, poke_id['name']);
        print("TUPLE(POKEMON_GENERIC): ",pokemon.name, pokemon.height, pokemon.weight)
        if populate_table:
            cur.execute(
                "INSERT INTO " +  table + " (" + table_id + ", name, height, weight, sprite) VALUES (%s, %s, %s, %s, %s)",
                (pokemon_index , pokemon.name, pokemon.height, pokemon.weight, pokemon.sprites.front_default,))

        #insert into child tables
        global pokemon_version_specificIndex
        for gameIndex in pokemon.game_indices:
            insertPokemonSpecificTable(cur, pb, gameIndex.version, pokemon.species.flavor_text_entries, pokemon_index, pokemon_version_specificIndex)
            pokemon_version_specificIndex += 1

        global pokemon_moveIndex
        for poke_move in pokemon.moves:
            for poke_move_version in poke_move.version_group_details:
                retval = insertPokemonMoveTable(cur,pb, poke_move.move, poke_move_version, pokemon_index, pokemon_moveIndex)
                pokemon_moveIndex = retval

        global pokemon_areaIndex
        for loc_area_enc in pokemon.location_area_encounters:
            for ver_enc_details in loc_area_enc.version_details:
                retval = insertPokemonAreaTable(cur, pb, loc_area_enc.location_area, ver_enc_details, pokemon_index, pokemon_areaIndex)
                pokemon_areaIndex = retval

        global pokemon_typeIndex
        for poke_type in pokemon.types:
            insertPokemonTypeTable(cur,pb, poke_type, pokemon_index, pokemon_typeIndex)
            pokemon_typeIndex += 1


        pokemon_index+=1
