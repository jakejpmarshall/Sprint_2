SELECT_CHARACTER = "SELECT * FROM charactercreator_character;"

AVG_ITEM_WEIGHT_PER_CHAR = '''
    SELECT cc_char.name, AVG(armory_item.weight) AS avg_item_weight 
    FROM charactercreator_character AS cc_char
    JOIN charactercreator_character_inventory AS cc_inv
    ON cc_char.character_id = cc_inv.character_id
    JOIN armory_item
    ON cc_inv.item_id = armory_item.item_id
    GROUP BY cc_char.character_id;
'''

CREATE_TEST_TABLE = '''
    CREATE TABLE IF NOT EXISTS test_table
    ("id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(200) NOT NULL,
    "age" INT NOT NULL,
    "country_of_origin" VARCHAR(200) NOT NULL);
'''

INSERT_TEST_TABLE = '''
    INSERT INTO test_table ("name", "age", "country_of_origin")
    VALUES ('Jake Marshall', 23, 'USA');
'''

DROP_TEST_TABLE = '''
    DROP TABLE IF EXISTS Test_table
'''

CREATE_CHARACTERS_TABLE = '''
    CREATE TABLE IF NOT EXISTS characters
    ("character_id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(30) NOT NULL,
    "level" INT NOT NULL,
    "exp" INT NOT NULL,
    "hp" INT NOT NULL,
    "strength" INT NOT NULL,
    "intelligence" INT NOT NULL,
    "dexterity" INT NOT NULL,
    "wisdom" INT NOT NULL)
'''
INSERT_CHARACTER_JAKE = '''
    INSERT INTO characters ("name", "level", "exp", "hp",
                            "strength", "intelligence",
                            "dexterity", "wisdom")
    VALUES ('Jake', 37, 105, 20, 5730, 100000, 283, 8284)
'''

DROP_CHARACTERS_TABLE = '''
    DROP TABLE IF EXISTS characters
'''
