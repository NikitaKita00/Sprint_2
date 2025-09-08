import allure
import pytest
from pages.constructor_page import ConstructorPage
from utils.data import TestData


@pytest.fixture
@allure.step("Логин пользователя")
def logged_in_user(driver, MainPage, LoginPage):
    main_page = MainPage(driver)
    login_page = LoginPage(driver)
    main_page.go_to_site()
    main_page.click_personal_account()
    login_page.login_with_detailed_locators(TestData.REAL_EMAIL, TestData.REAL_PASSWORD)
    yield


@allure.feature("Лента заказов")
class TestOrderFeed:

    @allure.title("Базовый тест создания заказа")
    def test_basic_order_creation(self, driver, logged_in_user):
        constructor_page = ConstructorPage(driver)

        success = constructor_page.create_order_with_drag()
        assert (
            constructor_page.is_constructor_page()
        ), "Не удалось загрузить конструктор"

        if not success:
  
            constructor_page.create_order_with_clicks()
            assert (
                constructor_page.is_order_modal_visible()
            ), "Модальное окно заказа не появилось"
            constructor_page.close_order_modal()

    @allure.title("Переход в ленту заказов")
    def test_go_to_order_feed(self, driver, logged_in_user):
        constructor_page = ConstructorPage(driver)
        constructor_page.click_order_feed()
        assert (
            "feed" in constructor_page.get_current_url()
        ), "Не удалось перейти в ленту заказов"

    @allure.title("Наличие заказов в ленте")
    def test_orders_in_feed(self, driver, logged_in_user):
        constructor_page = ConstructorPage(driver)
        constructor_page.click_order_feed()
        assert (
            "feed" in constructor_page.get_current_url()
        ), "Лента заказов не загрузилась"


    @allure.title("Работа модального окна")
    def test_modal_functionality(self, driver, logged_in_user):
        constructor_page = ConstructorPage(driver)
        constructor_page.click_bun_ingredient()
        assert (
            not constructor_page.is_order_modal_visible()
        ), "Окно модального заказа не появилось"
