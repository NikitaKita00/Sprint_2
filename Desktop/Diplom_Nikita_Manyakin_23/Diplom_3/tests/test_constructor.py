import allure
import pytest
from pages.constructor_page import ConstructorPage
from utils.data import TestData


@pytest.fixture
@allure.step("Логин пользователя")
def logged_in_user(driver):
    main_page = MainPage(driver)
    login_page = LoginPage(driver)
    main_page.go_to_site()
    main_page.click_personal_account()
    login_page.login_with_detailed_locators(TestData.REAL_EMAIL, TestData.REAL_PASSWORD)
    yield


@allure.feature("Основной функционал")
class TestConstructor:

    @allure.title("Открытие и закрытие модального окна с деталями ингредиента")
    def test_ingredient_modal(self, driver, logged_in_user):
        constructor = ConstructorPage(driver)
        constructor.click_ingredient()
        constructor.wait_for_modal_visible()
        assert constructor.is_modal_visible(), "Модальное окно не открылось"
        constructor.close_modal()
        constructor.wait_for_modal_hidden()
        assert not constructor.is_modal_visible(), "Модальное окно не закрылось"
