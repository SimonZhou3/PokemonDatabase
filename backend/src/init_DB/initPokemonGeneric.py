from init_DB.initPokemonSpecific import insert as insertPokemonSpecificTable
from init_DB.initPokemonMove import insert as insertPokemonMoveTable
from init_DB.initPokemonArea import insert as insertPokemonAreaTable
from init_DB.initPokemonType import insert as insertPokemonTypeTable
from init_DB.initPokemonItem import insert as insertPokemonItemTable
from init_DB.initPokemonStat import insert as insertPokemonStatTable

# change this according to API resource names
api_name = "pokemon"
table = "pokemon_generic"
table_id = table + "_id"
# parent = ""
# fk_id = parent+"_id"

populate_table = True

POKEDEX_SIZE = 905

# index for child id
pokemon_version_specificIndex = 1
pokemon_moveIndex = 1
pokemon_areaIndex = 1
pokemon_typeIndex = 1
pokemon_itemIndex = 1
pokemon_statIndex = 1

pokemon_version_array_after_white_2 = ['x', 'y', 'omega ruby', 'alpha sapphire', 'sun', 'moon', 'ultra sun',
                                       'ultra moon', 'sword', 'shield','legends arceus']


def init(cur, pb):
    global populate_table

    # create tables of dependent entities

    # get list of pokemon
    pokemonList = pb.APIResourceList(api_name)
    pokemon_index = 1
    for poke_id in pokemonList:
        # insert into pokemon table
        if (pokemon_index <= POKEDEX_SIZE):
            pokemon = pb.APIResource(api_name, poke_id['name']);
            print("TUPLE(POKEMON_GENERIC): ", pokemon.name, pokemon.height, pokemon.weight)
            if populate_table:
                cur.execute(
                    "INSERT INTO " + table + " (" + " name, height, weight, sprite) VALUES (%s, %s, %s, %s)",
                    (pokemon.name, pokemon.height, pokemon.weight, pokemon.sprites.front_default,))
            # insert into child tables
            global pokemon_statIndex
            insertPokemonStatTable(cur,pb,pokemon.stats, pokemon_index, 0)
            pokemon_statIndex += 1

            global pokemon_version_specificIndex
            if len(pokemon.game_indices) > 0:
                for gameIndex in pokemon.game_indices:
                    insertPokemonSpecificTable(cur, pb, gameIndex.version, pokemon.species.flavor_text_entries,
                                               pokemon_index, pokemon_version_specificIndex)
                    pokemon_version_specificIndex += 1
            else:
                if  650 <= pokemon_index <= 721:
                    insertPokemonSpecificTable(cur, pb, 'x', pokemon.species.flavor_text_entries, pokemon_index, pokemon_index)
                    insertPokemonSpecificTable(cur, pb, 'y', pokemon.species.flavor_text_entries, pokemon_index, pokemon_index)
                    pokemon_version_specificIndex += 2

                elif  722 <= pokemon_index <= 809:
                    insertPokemonSpecificTable(cur, pb, 'sun', pokemon.species.flavor_text_entries, pokemon_index, pokemon_index)
                    insertPokemonSpecificTable(cur, pb, 'moon', pokemon.species.flavor_text_entries, pokemon_index, pokemon_index)
                    insertPokemonSpecificTable(cur, pb, 'ultra sun', pokemon.species.flavor_text_entries, pokemon_index, pokemon_index)
                    insertPokemonSpecificTable(cur, pb, 'ultra moon', pokemon.species.flavor_text_entries, pokemon_index, pokemon_index)
                    pokemon_version_specificIndex += 4

                elif 810 <= pokemon_index <= 905:
                    insertPokemonSpecificTable(cur, pb, 'sword', pokemon.species.flavor_text_entries, pokemon_index, pokemon_index)
                    insertPokemonSpecificTable(cur, pb, 'shield', pokemon.species.flavor_text_entries, pokemon_index, pokemon_index)
                    pokemon_version_specificIndex += 2

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

            global pokemon_itemIndex
            for poke_held_item in pokemon.held_items:
                for poke_held_item_version in poke_held_item.version_details:
                    insertPokemonItemTable(cur,pb, poke_held_item.item, poke_held_item_version, pokemon_index, pokemon_itemIndex)
                    pokemon_itemIndex += 1

            pokemon_index += 1
        else:
            break

