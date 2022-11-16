CREATE TABLE IF NOT EXISTS generation (
    generation_id SERIAL PRIMARY KEY,
    name text UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS version_group (
    version_group_id SERIAL PRIMARY KEY,
    name text NOT NULL,
    generation_id integer,
    CONSTRAINT fk_generation_id FOREIGN KEY(generation_id) REFERENCES generation(generation_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS version (
    version_id SERIAL PRIMARY KEY,
    name text NOT NULL,
    release_date date,
    version_group_id integer NOT NULL,
    CONSTRAINT fk_version_group_id FOREIGN KEY(version_group_id) REFERENCES version_group(version_group_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS region (
    region_id SERIAL PRIMARY KEY,
    name text NOT NULL,
  generation_id integer NOT NULL,
  CONSTRAINT fk_generation_id FOREIGN KEY(generation_id) REFERENCES generation(generation_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS location (
    location_id SERIAL PRIMARY KEY,
    name text NOT NULL,
    region_id integer NOT NULL,
    CONSTRAINT fk_region_id FOREIGN KEY(region_id) REFERENCES region(region_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS area (
    area_id SERIAL PRIMARY KEY,
    name text NOT NULL,
    location_id integer NOT NULL,
    CONSTRAINT fk_location_id FOREIGN KEY(location_id) REFERENCES location(location_id)
);

CREATE TABLE IF NOT EXISTS item (
    item_id SERIAL PRIMARY KEY,
    name text NOT NULL,
    cost integer,
    category integer,
    description text,
    sprite text
);

CREATE TABLE IF NOT EXISTS type (
    type_id SERIAL PRIMARY KEY,
    name text NOT NULL
);

CREATE TABLE IF NOT EXISTS move (
    move_id SERIAL PRIMARY KEY,
    type_id integer NOT NULL,
    name text,
    accuracy integer,
    effect_chance integer,
    pp integer,
    priority integer,
    power integer,
    damage_class text,
    effect text,
    CONSTRAINT fk_type_id FOREIGN KEY(type_id) REFERENCES type(type_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS pokemon_generic (
    pokemon_generic_id SERIAL PRIMARY KEY,
    name text,
    height integer,
    weight integer,
    sprite text
);

CREATE TABLE IF NOT EXISTS pokemon_specific (
    pokemon_specific_id SERIAL UNIQUE,
    pokemon_generic_id integer,
    version_id integer,
    description text,
    PRIMARY KEY (pokemon_generic_id, version_id),
    CONSTRAINT fk_pokemon_generic_id FOREIGN KEY(pokemon_generic_id) REFERENCES pokemon_generic(pokemon_generic_id) ON DELETE CASCADE,
    CONSTRAINT fk_version_id FOREIGN KEY(version_id) REFERENCES version(version_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS pokemon_move (
    pokemon_move_id SERIAL PRIMARY KEY,
    pokemon_specific_id integer NOT NULL,
    move_id integer NOT NULL,
    method text,
    level integer,
    FOREIGN KEY(pokemon_specific_id) REFERENCES pokemon_specific(pokemon_specific_id) ON DELETE CASCADE,
    FOREIGN KEY(move_id) REFERENCES  move(move_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS pokemon_area (
    pokemon_area_id SERIAL PRIMARY KEY,
    pokemon_specific_id integer NOT NULL,
    area_id integer NOT NULL,
    max_chance integer,
    FOREIGN KEY(pokemon_specific_id) REFERENCES pokemon_specific(pokemon_specific_id) ON DELETE CASCADE,
    FOREIGN KEY(area_id) REFERENCES  area(area_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS pokemon_type (
    pokemon_type_id SERIAL PRIMARY KEY,
    slot integer,
    pokemon_generic_id integer NOT NULL,
    type_id integer NOT NULL,
    CONSTRAINT type_id FOREIGN KEY(type_id) REFERENCES type(type_id),
    CONSTRAINT fk_pokemon_generic_id FOREIGN KEY(pokemon_generic_id) REFERENCES pokemon_generic(pokemon_generic_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS pokemon_item (
    pokemon_item_id SERIAL PRIMARY KEY,
    pokemon_specific_id integer NOT NULL,
    item_id integer NOT NULL ,
    CONSTRAINT type_id FOREIGN KEY(item_id) REFERENCES item(item_id) ON DELETE CASCADE,
    CONSTRAINT fk_pokemon_specific_id FOREIGN KEY(pokemon_specific_id) REFERENCES pokemon_specific(pokemon_specific_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS pokemon_stat (
    pokemon_generic_id SERIAL PRIMARY KEY,
    hp integer,
    attack integer,
    defence integer,
    special_attack integer,
    special_defence integer,
    speed integer,
    CONSTRAINT fk_pokemon_generic_id FOREIGN KEY(pokemon_generic_id) REFERENCES pokemon_generic(pokemon_generic_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS trainer (
    trainer_id SERIAL PRIMARY KEY,
    name text NOT NULL
);

CREATE TABLE IF NOT EXISTS trained_pokemon (
    pokemon_specific_id SERIAL,
    version_id integer,
    trainer_id integer,
    nickname text,
    PRIMARY KEY (pokemon_specific_id,version_id,trainer_id),
    CONSTRAINT fk_pokemon_specific_id FOREIGN KEY(pokemon_specific_id) REFERENCES pokemon_specific(pokemon_specific_id) ON DELETE CASCADE,
    CONSTRAINT fk_version_id FOREIGN KEY(version_id) REFERENCES version(version_id) ON DELETE CASCADE,
    CONSTRAINT fk_trainer_id FOREIGN KEY(trainer_id) REFERENCES trainer(trainer_id) ON DELETE CASCADE
);