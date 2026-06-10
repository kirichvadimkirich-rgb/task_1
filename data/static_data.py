from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

# Для Bun: тестируем имя (цена фиксирована) и цену (имя фиксировано)
BUN_NAMES = ["булочка", "Черный рыцарь", "", "Black burger", "Пышка Премьер"]
FIXED_BUN_PRICE = 100.0

BUN_PRICES = [0.0, 0.01, 50.0, 100.5, 999999.99]
FIXED_BUN_NAME = "Тестовая булочка"

INGREDIENT_POSITIVE_DATA = [
    (INGREDIENT_TYPE_SAUCE, "сырный", 100),
    (INGREDIENT_TYPE_FILLING, "cutlet", 150.5),
    (INGREDIENT_TYPE_SAUCE, "", 0),
    (INGREDIENT_TYPE_FILLING, "курица", 0.01),
]