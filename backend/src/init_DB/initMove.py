#change this according to API resource names\
api_name = "move"
table = api_name
table_id = table+"_id"
parent = "type"
fk_id = parent+"_id"

populate_table = True

#index for child id
child_id = 1

def insert(cur, pb, move, type_id, id):
    if populate_table:
        if len(move.effect_entries) > 0:
            effect = move.effect_entries[0].effect.replace("$effect_chance%", str(move.effect_chance))
        else:
            effect = move.flavor_text_entries[7].flavor_text
        print("TUPLE(MOVE) :", id, move.name, type_id, move.accuracy, move.effect_chance, move.pp, move.priority, move.power, move.damage_class.name, effect)
        cur.execute(
            "INSERT INTO " + table + " (" + fk_id + ", name, accuracy, effect_chance, pp, priority, power, damage_class, effect) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (type_id, move.name, move.accuracy, move.effect_chance, move.pp, move.priority, move.power, move.damage_class.name, effect))

