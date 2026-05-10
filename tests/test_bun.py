import pytest
from praktikum.bun import Bun
from data.static_data import BUN_POSITIVE_DATA
import allure


@allure.feature('Булочки для бургера')
class TestBun:

    @allure.title('Получение названия булочки')
    @allure.description('Проверка, что метод get_name() возвращает корректное имя булочки для различных позитивных случаев '
    '(обычное имя, пустая строка, экзотические названия)')
    @pytest.mark.parametrize('name, price', BUN_POSITIVE_DATA)
    def test_bun_get_name_positive(self, name, price):
        with allure.step(f'Создать булочку с именем "{name}" и ценой {price}'):
            bun = Bun(name, price)

        with allure.step('Проверить, что get_name() возвращает ожидаемое имя'):
            assert bun.get_name() == name
    
    @allure.title('Получение цены булочки')
    @allure.description('Проверка, что метод get_price() возвращает корректную цену булочки '
    '(целые и дробные числа, включая граничные значения 0.0, 0.01 и большие суммы)')
    @pytest.mark.parametrize('name, price', BUN_POSITIVE_DATA)
    def test_bun_get_price_positive(self, name, price):
        with allure.step(f'Создать булочку с именем "{name}" и ценой {price}'):
            bun = Bun(name, price)

        with allure.step('Проверить, что get_price() возвращает ожидаемую цену'):
            assert bun.get_price() == price