from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

BUN_POSITIVE_DATA = [
    ("булочка", 50.0),
    ("Черный рыцарь", 100.5),
    ("", 0.0),          
    ("Black burger", 0.01),   
    ("Пышка Премьер", 999999.99) 
]

INGREDIENT_POSITIVE_DATA = [
    (INGREDIENT_TYPE_SAUCE, "сырный", 100),
    (INGREDIENT_TYPE_FILLING, "cutlet", 150.5),
    (INGREDIENT_TYPE_SAUCE, "", 0),
    (INGREDIENT_TYPE_FILLING, "курица", 0.01),
]