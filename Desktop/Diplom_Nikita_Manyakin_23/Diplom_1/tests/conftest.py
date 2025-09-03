import pytest
from unittest.mock import Mock
from tests.helpers.mocks import create_mock_bun, create_mock_ingredient


@pytest.fixture
def mock_bun():
    return create_mock_bun()


@pytest.fixture
def mock_ingredient_sauce():
    return create_mock_ingredient(name="test_sauce", ingredient_type="SAUCE")


@pytest.fixture
def mock_ingredient_filling():
    return create_mock_ingredient(name="test_filling", ingredient_type="FILLING")


@pytest.fixture
def mock_ingredient():
    return create_mock_ingredient()


@pytest.fixture
def burger_with_ingredients(mock_bun, mock_ingredient_sauce, mock_ingredient_filling):
    from praktikum.burger import Burger

    burger = Burger()
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_ingredient_sauce)
    burger.add_ingredient(mock_ingredient_filling)
    return burger
