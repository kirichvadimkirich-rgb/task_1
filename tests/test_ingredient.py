import pytest
from praktikum.ingredient import Ingredient
from data.static_data import INGREDIENT_POSITIVE_DATA
import allure

@allure.feature('Ингредиенты для бургера')
class TestIngredient:

    @allure.title('Получение типа ингредиента')
    @allure.description('Проверка, что метод get_type() возвращает корректный тип ингредиента '
                        '(соус или начинка) для различных позитивных случаев '
                        '(разные типы, имена, цены, включая граничные значения)')
    @pytest.mark.parametrize('ingredient_type, name, price', INGREDIENT_POSITIVE_DATA)
    def test_get_type(self, ingredient_type, name, price):
        with allure.step(f'Создать ингредиент с типом "{ingredient_type}", c именем "{name}" и ценой {price}'):
            ingredient = Ingredient(ingredient_type, name, price)

        with allure.step('Проверить, что get_type() возвращает ожидаемый тип'):    
            assert ingredient.get_type() == ingredient_type

    @allure.title('Получение названия ингредиента')
    @allure.description('Проверка, что метод get_name() возвращает корректное имя ингредиента '
                        '(обычное имя, пустая строка, экзотические названия)')
    @pytest.mark.parametrize('ingredient_type, name, price', INGREDIENT_POSITIVE_DATA)
    def test_get_name(self, ingredient_type, name, price):
        with allure.step(f'Создать ингредиент с типом "{ingredient_type}", c именем "{name}" и ценой {price}'):
            ingredient = Ingredient(ingredient_type, name, price)

        with allure.step('Проверить, что get_name() возвращает ожидаемое имя'):    
            assert ingredient.get_name() == name

    @allure.title('Получение цены ингредиента')
    @allure.description('Проверка, что метод get_price() возвращает корректную цену ингредиента '
                        '(целые и дробные числа, включая граничные значения 0, 0.01)')
    @pytest.mark.parametrize('ingredient_type, name, price', INGREDIENT_POSITIVE_DATA)
    def test_get_price(self, ingredient_type, name, price):
        with allure.step(f'Создать ингредиент с типом "{ingredient_type}", c именем "{name}" и ценой {price}'):
            ingredient = Ingredient(ingredient_type, name, price)

        with allure.step('Проверить, что get_price() возвращает ожидаемую цену'):
            assert ingredient.get_price() == price