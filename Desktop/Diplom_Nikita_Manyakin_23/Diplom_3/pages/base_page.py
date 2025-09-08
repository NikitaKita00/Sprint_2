import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Ожидание видимости элемента: {locator}")
    def wait_until_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Ожидание кликабельности элемента: {locator}")
    def wait_until_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    @allure.step("Ожидание исчезновения элемента: {locator}")
    def wait_until_invisible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )

    @allure.step("Поиск одного элемента: {locator}")
    def find_element(self, locator, timeout=10):
        return self.wait_until_visible(locator, timeout)

    @allure.step("Поиск нескольких элементов: {locator}")
    def find_elements(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_all_elements_located(locator)
        )

    @allure.step("Клик по элементу: {locator}")
    def click(self, locator, timeout=10):
        element = self.wait_until_clickable(locator, timeout)
        element.click()

    @allure.step("Ввод текста '{text}' в элемент: {locator}")
    def send_keys(self, locator, text, timeout=10):
        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(text)

    @allure.step("Проверка видимости элемента: {locator}")
    def is_element_visible(self, locator, timeout=3):
        try:
            self.find_element(locator, timeout)
            return True
        except TimeoutException:
            return False

    @allure.step("Ожидание URL, содержащего текст: {text}")
    def wait_for_url_contains(self, text, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.url_contains(text))

    @allure.step("Ожидание фиксированное {seconds} секунд")
    def wait_for(self, seconds):
        self.driver.implicitly_wait(seconds)
