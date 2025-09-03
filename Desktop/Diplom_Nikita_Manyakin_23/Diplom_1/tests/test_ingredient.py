import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:
    """Тесты для класса Ingredient"""
    
    @pytest.mark.parametrize("ingredient_type,name,price", [
        (INGREDIENT_TYPE_SAUCE, "hot sauce", 100.0),
        (INGREDIENT_TYPE_SAUCE, "sour cream", 200.0),
        (INGREDIENT_TYPE_FILLING, "cutlet", 150.0),
        (INGREDIENT_TYPE_FILLING, "dinosaur", 250.0),
        ("UNKNOWN", "test", 0.0)
    ])
    def test_ingredient_creation(self, ingredient_type, name, price):
        """Тестирование создания ингредиента с разными параметрами"""
        ingredient = Ingredient(ingredient_type, name, price)
        
        assert ingredient.get_type() == ingredient_type
        assert ingredient.get_name() == name
        assert ingredient.get_price() == price
    
    def test_ingredient_name_type(self):
        """Тестирование типа возвращаемого имени"""
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "test", 100)
        assert isinstance(ingredient.get_name(), str)
    
    def test_ingredient_price_type(self):
        """Тестирование типа возвращаемой цены"""
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "test", 100.5)
        assert isinstance(ingredient.get_price(), float)
    
    def test_ingredient_type_type(self):
        """Тестирование типа возвращаемого типа ингредиента"""
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "test", 100)
        assert isinstance(ingredient.get_type(), str)