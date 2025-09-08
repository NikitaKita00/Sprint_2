from selenium.webdriver.common.by import By


class ConstructorLocators:
 
    CONSTRUCTOR_BUTTON = (By.XPATH, "//nav//a[@href='/constructor']//p")
    ORDER_FEED_BUTTON = (By.XPATH, "//nav//a[@href='/order-feed']//p")
    ANY_INGREDIENT = (By.CSS_SELECTOR, "a.BurgerIngredient_ingredient__")

    BUN_INGREDIENT = (
        By.XPATH,
        "//a[contains(@class, 'BurgerIngredient_ingredient__') and .//span[text()='Булка']]",  # пример с текстом
    )
    SAUCE_INGREDIENT = (
        By.XPATH,
        "//a[contains(@class, 'BurgerIngredient_ingredient__') and .//span[text()='Соус']]",
    )
    FILLING_INGREDIENT = (
        By.XPATH,
        "//a[contains(@class, 'BurgerIngredient_ingredient__') and .//span[text()='Начинка']]",
    )


    DRAGGABLE_INGREDIENT = (
        By.CSS_SELECTOR,
        "a.BurgerIngredient_ingredient__[draggable='true']",
    )

    INGREDIENT_COUNTER = (By.CSS_SELECTOR, "div.counter_counter__")


    MODAL_WINDOW = (By.CSS_SELECTOR, "section.Modal_modal__ > div")
    MODAL_CLOSE_BUTTON = (By.CSS_SELECTOR, "section.Modal_modal__ button.Modal_close__")


    MODAL_OVERLAY = (By.CSS_SELECTOR, "div.Modal_modal_overlay__")
    MODAL_CONTENT = (By.CSS_SELECTOR, "div.Modal_modal__")
    MODAL_CLOSE_ALT = (By.CSS_SELECTOR, "button.Modal_close__")


    BURGER_CONSTRUCTOR = (By.CSS_SELECTOR, "section.BurgerConstructor_basket__")

    ORDER_BUTTON = (By.CSS_SELECTOR, "section.BurgerConstructor_basket__ button")
    ORDER_TOTAL = (By.CSS_SELECTOR, "section.BurgerConstructor_basket__ p")

  
    ORDER_MODAL = (By.CSS_SELECTOR, "div.Modal_modal__")
    ORDER_NUMBER = (By.XPATH, "//h2[contains(@class, 'Modal_order')]")
