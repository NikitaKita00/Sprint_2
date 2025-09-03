from unittest.mock import Mock


def create_mock_bun(name="test_bun", price=100):
    """Создает мок булочки"""
    mock = Mock()
    mock.get_name.return_value = name
    mock.get_price.return_value = price
    return mock


def create_mock_ingredient(name="test_ingredient", price=50, ingredient_type="SAUCE"):
    """Создает мок ингредиента"""
    mock = Mock()
    mock.get_name.return_value = name
    mock.get_price.return_value = price
    mock.get_type.return_value = ingredient_type
    return mock


def create_mock_burger_with_ingredients():
    """Создает мок бургера с ингредиентами"""
    mock_burger = Mock()
    mock_burger.get_price.return_value = 300
    mock_burger.get_receipt.return_value = "Test Receipt"
    return mock_burger
