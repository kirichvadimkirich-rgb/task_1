
from praktikum.database import Database
import allure


@allure.feature('База данных')
class TestDatabase:
    def setup_method(self):
        #Создаём свежую базу данных перед каждым тестом
        with allure.step('Инициализация базы данных'):
            self.db = Database()

    @allure.title('Проверка, что available_buns() возвращает список')
    @allure.description('Метод available_buns() должен возвращать объект типа list. '
                        'Тест проверяет, что метод не возвращает None и возвращает список.')
    def test_available_buns_returns_list(self):
        buns = self.db.available_buns()
        assert isinstance(buns, list)

    @allure.title('Проверка, что available_ingredients() возвращает список')
    @allure.description('Метод available_ingredients() должен возвращать объект типа list. '
                        'Тест проверяет, что метод не возвращает None и возвращает список.')
    def test_available_ingredients_returns_list(self):
        ingredients = self.db.available_ingredients()
        assert isinstance(ingredients, list)
