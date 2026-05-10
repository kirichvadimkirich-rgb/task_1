
from praktikum.database import Database
import allure


@allure.feature('База данных')
class TestDatabase:
    def setup_method(self):
        #Создаём свежую базу данных перед каждым тестом
        with allure.step('Инициализация базы данных'):
            self.db = Database()

    @allure.title('Количество доступных булок')
    @allure.description('Проверка, что метод available_buns() возвращает ровно 3 булочки (black, white, red)')
    def test_available_buns_count(self):
        with allure.step('Получить список булок из базы данных'):
            buns = self.db.available_buns()

        with allure.step('Проверить, что количество булок равно 3'):
            assert len(buns) == 3

    @allure.title('Названия доступных булок')
    @allure.description('Проверка, что названия булок соответствуют ожидаемому порядку: black bun, white bun, red bun')
    def test_available_buns_names(self):
        with allure.step('Получить список булок'):
            buns = self.db.available_buns()
        with allure.step('Извлечь названия булок'):    
            names = [bun.get_name() for bun in buns]

        with allure.step('Сравнить названия со списком'):
            assert names == ["black bun", "white bun", "red bun"]

    @allure.title('Цены доступных булок')
    @allure.description('Проверка, что цены булок соответствуют ожидаемым: 100, 200, 300')
    def test_available_buns_prices(self):
        with allure.step('Получить список булок'):
            buns = self.db.available_buns()
        with allure.step('Извлечь цены с помощью get_price()'):
            prices = [bun.get_price() for bun in buns]

        with allure.step('Сравнить цены со списком [100, 200, 300]'):
            assert prices == [100, 200, 300]

    @allure.title('Количество доступных ингредиентов')
    @allure.description('Проверка, что метод available_ingredients() возвращает ровно 6 ингредиентов (3 соуса и 3 начинки)')
    def test_available_ingredients_count(self):
        with allure.step('Получить список ингредиентов из базы данных'):
            ingredients = self.db.available_ingredients()
        with allure.step('Проверить, что количество ингредиентов равно 6'):
            assert len(ingredients) == 6

    