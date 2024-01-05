q1 = "SELECT character_id, name FROM charactercreator_character;"

AVG_ITEM_WEIGHT_PER_CHAR = '''
SELECT cc_char.name, AVG(armory_item.weight) AS avg_item_weight 
FROM charactercreator_character AS cc_char
JOIN charactercreator_character_inventory AS cc_inv
ON cc_char.character_id = cc_inv.character_id
JOIN armory_item
ON cc_inv.item_id = armory_item.item_id
GROUP BY cc_char.character_id
'''