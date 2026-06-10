import pytest
from praktikum.bun import Bun
from data.static_data import BUN_NAMES, FIXED_BUN_PRICE, BUN_PRICES, FIXED_BUN_NAME
import allure


@allure.feature('Булочки для бургера')
class TestBun:

    @allure.title('Получение названия булочки')
    @allure.description('Проверка, что метод get_name() возвращает корректное имя булочки для различных позитивных случаев '
    '(обычное имя, пустая строка, экзотические названия). Имя меняется, цена фиксирована.')
    @pytest.mark.parametrize('name', BUN_NAMES)
    def test_bun_get_name_positive(self, name):
        with allure.step(f'Создать булочку с именем "{name}" и фиксированной ценой {FIXED_BUN_PRICE}'):
            bun = Bun(name, FIXED_BUN_PRICE)

        with allure.step('Проверить, что get_name() возвращает ожидаемое имя'):
            assert bun.get_name() == name
    
    @allure.title('Получение цены булочки')
    @allure.description('Проверка, что метод get_price() возвращает корректную цену булочки '
    '(целые и дробные числа, включая граничные значения 0.0, 0.01 и большие суммы). Цена меняется, имя фиксировано.')
    @pytest.mark.parametrize('price', BUN_PRICES)
    def test_bun_get_price_positive(self, price):
        with allure.step(f'Создать булочку с фиксированным именем "{FIXED_BUN_NAME}" и ценой {price}'):
            bun = Bun(FIXED_BUN_NAME, price)

        with allure.step('Проверить, что get_price() возвращает ожидаемую цену'):
            assert bun.get_price() == price