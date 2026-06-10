
from unittest.mock import Mock

import allure

@allure.feature('Бургер')
class TestBurger:

    @allure.title('Установка булочки в бургер')
    @allure.description('Проверка, что метод set_buns() сохраняет переданный объект булочки во внутреннее поле burger.bun. Используется мок.')
    def test_set_buns(self, burger):
        with allure.step('Создать мок-объект булочки'):
            mock_bun = Mock()
        with allure.step('Установить булочку в бургер'):
            burger.set_buns(mock_bun)
        with allure.step('Проверить, что поле burger.bun указывает на переданный мок'):
            assert burger.bun == mock_bun

    @allure.title('Добавление ингредиента в бургер')
    @allure.description('Проверка, что метод add_ingredient() добавляет ингредиент в конец списка ingredients. Используется мок.')
    def test_add_ingredient(self, burger):
        with allure.step('Создать мок-объект ингредиента'):
            mock_ing = Mock()
        with allure.step('Добавить ингредиент в бургер'):
            burger.add_ingredient(mock_ing)
        with allure.step('Проверить, что ингредиент присутствует в списке и длина списка равна 1'):
            assert mock_ing in burger.ingredients
            assert len(burger.ingredients) == 1

    @allure.title('Удаление ингредиента по индексу')
    @allure.description('Проверка, что remove_ingredient() удаляет ингредиент из списка по указанному индексу. Моки используются для имитации ингредиентов.')
    def test_remove_ingredient(self, burger):
        with allure.step('Создать два мок-ингредиента и установить их в список бургера'):
            ing1, ing2 = Mock(), Mock()
            burger.ingredients = [ing1, ing2]
        with allure.step('Удалить ингредиент с индексом 0'):
            burger.remove_ingredient(0)
        with allure.step('Проверить, что в списке остался только второй ингредиент'):
            assert burger.ingredients == [ing2]

    @allure.title('Перемещение ингредиента на новую позицию')
    @allure.description('Проверка, что move_ingredient() корректно перемещает ингредиент из одного индекса в другой. Моки используются.')
    def test_move_ingredient(self, burger):
        with allure.step('Создать три мок-ингредиента и задать начальный порядок [ing1, ing2, ing3]'):
            ing1, ing2, ing3 = Mock(), Mock(), Mock()
            burger.ingredients = [ing1, ing2, ing3]
        with allure.step('Переместить ингредиент с индекса 2 на индекс 0'):
            burger.move_ingredient(2, 0)
        with allure.step('Проверить, что порядок стал [ing3, ing1, ing2]'):
            assert burger.ingredients == [ing3, ing1, ing2]

    @allure.title('Расчёт общей стоимости бургера')
    @allure.description('Проверка, что get_price() правильно суммирует цену булочки (умноженную на 2) и цены всех ингредиентов. Все зависимости замоканы.')
    def test_get_price(self, burger):
        with allure.step('Создать мок-булочку с ценой 150'):
            mock_bun = Mock()
            mock_bun.get_price.return_value = 150
            burger.set_buns(mock_bun)
        with allure.step('Создать два мок-ингредиента с ценами 50 и 70 и добавить их в бургер'):
            mock_ing1 = Mock()
            mock_ing1.get_price.return_value = 50
            mock_ing2 = Mock()
            mock_ing2.get_price.return_value = 70
            burger.add_ingredient(mock_ing1)
            burger.add_ingredient(mock_ing2)
        with allure.step('Рассчитать ожидаемую цену: 150 * 2 + 50 + 70 = 420'):
            expected = 150 * 2 + 50 + 70
        with allure.step('Проверить, что get_price() вернул 420'):
            assert burger.get_price() == expected


