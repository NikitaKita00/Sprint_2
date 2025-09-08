import allure
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    TimeoutException,
)

from .base_page import BasePage
from locators.constructor_locators import ConstructorLocators


class ConstructorPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = ConstructorLocators()

    @allure.step("Клик по кнопке конструктор")
    def click_constructor(self):
        self.click(self.locators.CONSTRUCTOR_BUTTON)
        self.wait_for(seconds=2)

    @allure.step("Клик по кнопке ленты заказов")
    def click_order_feed(self):
        self.click(self.locators.ORDER_FEED_BUTTON)
        self.wait_for(seconds=2)

    @allure.step("Клик по ингредиенту")
    def click_ingredient(self):
        self.click(self.locators.INGREDIENT_ITEM)
        self.wait_for_modal_visible()

    @allure.step("Закрыть модальное окно")
    def close_modal(self):
        try:
            close_button = self.wait_until_clickable(
                self.locators.MODAL_CLOSE_BUTTON, timeout=5
            )
            close_button.click()
        except ElementClickInterceptedException:
            actions = ActionChains(self.driver)
            actions.send_keys(Keys.ESCAPE).perform()
        except TimeoutException:
            try:
                overlay = self.find_element(self.locators.MODAL_OVERLAY)
                self.driver.execute_script("arguments[0].click();", overlay)
            except Exception:
                pass
        self.wait_for_modal_hidden()

    @allure.step("Закрыть модальное окно клавишей ESC")
    def close_modal_with_esc(self):
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.ESCAPE).perform()
        self.wait_for_modal_hidden()

    @allure.step("Ожидать видимость модального окна")
    def wait_for_modal_visible(self, timeout=5):
        self.wait_until_visible(self.locators.MODAL_WINDOW, timeout)

    @allure.step("Ожидать скрытие модального окна")
    def wait_for_modal_hidden(self, timeout=5):
        self.wait_until_invisible(self.locators.MODAL_WINDOW, timeout)

    @allure.step("Перетащить ингредиент в конструктор")
    def drag_ingredient_to_constructor(self):
        try:
            source_element = self.find_element(self.locators.DRAGGABLE_INGREDIENT)
            target_element = self.find_element(self.locators.BURGER_CONSTRUCTOR)

            actions = ActionChains(self.driver)
            actions.drag_and_drop(source_element, target_element).perform()

            self.wait_for(seconds=2)
        except Exception as e:
            print(f"Ошибка при перетаскивании: {e}")
            try:
                source_element.click()
                self.wait_for(seconds=1)
                target_element.click()
                self.wait_for(seconds=1)
            except Exception:
                pass

    @allure.step("Перетащить ингредиент с offset")
    def drag_ingredient_with_offset(self):
        try:
            source_element = self.find_element(self.locators.DRAGGABLE_INGREDIENT)
            constructor_section = self.find_element(self.locators.BURGER_CONSTRUCTOR)

            loc = constructor_section.location
            size = constructor_section.size
            # Вычисляем центр целевой области
            target_x = loc["x"] + size["width"] // 2
            target_y = loc["y"] + size["height"] // 2

            actions = ActionChains(self.driver)
            actions.click_and_hold(source_element).pause(0.5)
            actions.move_by_offset(target_x, target_y).pause(0.5)
            actions.release().perform()

            self.wait_for(seconds=2)
        except Exception as e:
            print(f"Ошибка при перетаскивании с offset: {e}")

    @allure.step("Получить количество ингредиентов")
    def get_ingredient_counter(self, element):
        try:
            counter = element.find_element(*self.locators.INGREDIENT_COUNTER)
            return int(counter.text) if counter.text else 0
        except Exception:
            return 0

    @allure.step("Сделать заказ")
    def make_order(self):
        self.click(self.locators.ORDER_BUTTON)
        self.wait_for(seconds=3)

    @allure.step("Проверить видимость модального окна ингредиента")
    def is_modal_visible(self):
        return self.is_element_visible(self.locators.MODAL_WINDOW)

    @allure.step("Проверить видимость модального окна заказа")
    def is_order_modal_visible(self):
        return self.is_element_visible(self.locators.ORDER_MODAL)

    @allure.step("Проверить видимость страницы конструктора")
    def is_constructor_page(self):
        return self.is_element_visible(self.locators.BURGER_CONSTRUCTOR)

    @allure.step("Получить общую сумму заказа")
    def get_order_total(self):
        try:
            element = self.find_element(self.locators.ORDER_TOTAL)
            return element.text if element else "0"
        except Exception:
            return "0"
