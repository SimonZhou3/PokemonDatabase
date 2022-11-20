CREATE TABLE IF NOT EXISTS generation
(
    generation_id SERIAL PRIMARY KEY,
    name          text UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS version_group
(
    version_group_id SERIAL PRIMARY KEY,
    name             text NOT NULL,
    generation_id    integer,
    FOREIGN KEY (generation_id) REFERENCES generation (generation_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS version
(
    version_id       SERIAL PRIMARY KEY,
    name             text    NOT NULL,
    release_date     date,
    version_group_id integer NOT NULL,
    FOREIGN KEY (version_group_id) REFERENCES version_group (version_group_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS region
(
    region_id     SERIAL PRIMARY KEY,
    name          text    NOT NULL,
    generation_id integer NOT NULL,
    FOREIGN KEY (generation_id) REFERENCES generation (generation_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS location
(
    location_id SERIAL PRIMARY KEY,
    name        text    NOT NULL,
    region_id   integer NOT NULL,
    FOREIGN KEY (region_id) REFERENCES region (region_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS area
(
    area_id     SERIAL PRIMARY KEY,
    name        text    NOT NULL,
    location_id integer NOT NULL,
    FOREIGN KEY (location_id) REFERENCES location (location_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS item
(
    item_id     SERIAL PRIMARY KEY,
    name        text NOT NULL,
    cost        integer,
    category    text,
    description text,
    sprite      text
);

CREATE TABLE IF NOT EXISTS type
(
    type_id SERIAL PRIMARY KEY,
    name    text NOT NULL
);

CREATE TABLE IF NOT EXISTS move
(
    move_id       SERIAL PRIMARY KEY,
    type_id       integer NOT NULL,
    name          text,
    accuracy      integer,
    effect_chance integer,
    pp            integer,
    priority      integer,
    power         integer,
    damage_class  text,
    effect        text,
    FOREIGN KEY (type_id) REFERENCES type (type_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS pokemon_generic
(
    pokemon_generic_id SERIAL PRIMARY KEY,
    name               text,
    height             integer,
    weight             integer,
    sprite             text
);

CREATE TABLE IF NOT EXISTS pokemon_specific
(
    pokemon_specific_id SERIAL UNIQUE,
    pokemon_generic_id  integer,
    version_id          integer,
    description         text,
    PRIMARY KEY (pokemon_generic_id, version_id),
    FOREIGN KEY (pokemon_generic_id) REFERENCES pokemon_generic (pokemon_generic_id) ON DELETE CASCADE,
    FOREIGN KEY (version_id) REFERENCES version (version_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS pokemon_move
(
    pokemon_move_id     SERIAL PRIMARY KEY,
    pokemon_specific_id integer NOT NULL,
    move_id             integer NOT NULL,
    method              text,
    level               integer,
    FOREIGN KEY (pokemon_specific_id) REFERENCES pokemon_specific (pokemon_specific_id) ON DELETE CASCADE,
    FOREIGN KEY (move_id) REFERENCES move (move_id) ON DELETE CASCADE
);


/* TODO -- NEED ASSERTIONS */
CREATE TABLE IF NOT EXISTS pokemon_area
(
    pokemon_area_id     SERIAL PRIMARY KEY,
    pokemon_specific_id integer NOT NULL,
    area_id             integer NOT NULL,
    max_chance          integer,
    FOREIGN KEY (pokemon_specific_id) REFERENCES pokemon_specific (pokemon_specific_id) ON DELETE CASCADE,
    FOREIGN KEY (area_id) REFERENCES area (area_id) ON DELETE CASCADE
);


/* TODO -- NEED ASSERTIONS */
CREATE TABLE IF NOT EXISTS pokemon_type
(
    pokemon_type_id    SERIAL PRIMARY KEY,
    slot               integer,
    pokemon_generic_id integer NOT NULL,
    type_id            integer NOT NULL,
    FOREIGN KEY (type_id) REFERENCES type (type_id),
    FOREIGN KEY (pokemon_generic_id) REFERENCES pokemon_generic (pokemon_generic_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS pokemon_item
(
    pokemon_item_id     SERIAL PRIMARY KEY,
    pokemon_specific_id integer NOT NULL,
    item_id             integer NOT NULL,
    rarity              integer,
    FOREIGN KEY (item_id) REFERENCES item (item_id) ON DELETE CASCADE,
    FOREIGN KEY (pokemon_specific_id) REFERENCES pokemon_specific (pokemon_specific_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS pokemon_stat
(
    pokemon_stat_id    SERIAL,
    pokemon_generic_id SERIAL PRIMARY KEY,
    hp                 integer,
    attack             integer,
    defence            integer,
    special_attack     integer,
    special_defence    integer,
    speed              integer,
    FOREIGN KEY (pokemon_generic_id) REFERENCES pokemon_generic (pokemon_generic_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS trainer
(
    trainer_id SERIAL PRIMARY KEY,
    gender text,
    name       text NOT NULL
);

CREATE TABLE IF NOT EXISTS trained_pokemon
(
    trained_pokemon_id  SERIAL,
    pokemon_specific_id integer,
    trainer_id          integer,
    nickname            text,
    level               integer,
    PRIMARY KEY (trained_pokemon_id, pokemon_specific_id, trainer_id),
    FOREIGN KEY (pokemon_specific_id) REFERENCES pokemon_specific (pokemon_specific_id) ON DELETE CASCADE,
    FOREIGN KEY (trainer_id) REFERENCES trainer (trainer_id) ON DELETE CASCADE
);

CREATE FUNCTION check_pokemon_type() RETURNS trigger AS $check_pokemon_type$
    declare type_size integer;
    declare t1_type_id integer;
    declare t2_type_id integer;

    BEGIN
        SELECT COUNT(*) into type_size FROM pokemon_type WHERE pokemon_generic_id = NEW.pokemon_generic_id;
        SELECT type_id into t1_type_id FROM pokemon_type WHERE pokemon_generic_id = NEW.pokemon_generic_id OFFSET 0;
        SELECT type_id into t2_type_id FROM pokemon_type WHERE pokemon_generic_id = NEW.pokemon_generic_id OFFSET 1;

        raise notice 'Count type: %', type_size;
        raise notice 'Value: %', t1_type_id;
        raise notice 'Value: %', t2_type_id;
        IF type_size = 2 THEN
            RAISE EXCEPTION 'Unable to insert more than 2 types for a Pokemon';
        END IF;
        IF (t1_type_id IS NOT NULL AND t1_type_id = NEW.type_id) OR (t2_type_id IS NOT NULL AND t2_type_id = NEW.type_id) THEN
            RAISE EXCEPTION ' Duplicate Typing found ';
        END IF;
    RETURN NEW;
    END;
$check_pokemon_type$ LANGUAGE plpgsql;

 CREATE TRIGGER check_type
     BEFORE INSERT ON pokemon_type
     FOR EACH ROW
     EXECUTE FUNCTION check_pokemon_type();


