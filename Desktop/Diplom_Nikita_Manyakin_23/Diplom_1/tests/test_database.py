import pytest
from praktikum.database import Database


class TestDatabase:
    """Тесты для класса Database"""

    def test_available_buns(self):
        """Тестирование получения доступных булочек"""
        database = Database()
        buns = database.available_buns()

        assert len(buns) == 3
        assert all(bun.__class__.__name__ == "Bun" for bun in buns)

    def test_available_ingredients(self):
        """Тестирование получения доступных ингредиентов"""
        database = Database()
        ingredients = database.available_ingredients()

        assert len(ingredients) == 6
        assert all(
            ingredient.__class__.__name__ == "Ingredient" for ingredient in ingredients
        )

    def test_available_buns_has_correct_items(self):
        """Тестирование что булочки содержат правильные элементы"""
        database = Database()
        buns = database.available_buns()

        bun_names = [bun.get_name() for bun in buns]
        assert "black bun" in bun_names
        assert "white bun" in bun_names
        assert "red bun" in bun_names

    def test_available_ingredients_has_correct_items(self):
        """Тестирование что ингредиенты содержат правильные элементы"""
        database = Database()
        ingredients = database.available_ingredients()

        ingredient_names = [ing.get_name() for ing in ingredients]
        assert "hot sauce" in ingredient_names
        assert "cutlet" in ingredient_names
