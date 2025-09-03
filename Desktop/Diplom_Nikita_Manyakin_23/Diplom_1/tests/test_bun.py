import pytest
from praktikum.bun import Bun


class TestBun:
    """Тесты для класса Bun"""

    @pytest.mark.parametrize(
        "name,price",
        [
            ("black bun", 100.0),
            ("white bun", 200.0),
            ("red bun", 300.0),
            ("", 0.0),
            ("special bun", 999.99),
        ],
    )
    def test_bun_creation(self, name, price):
        """Тестирование создания булочки с разными параметрами"""
        bun = Bun(name, price)

        assert bun.get_name() == name
        assert bun.get_price() == price

    def test_bun_name_type(self):
        """Тестирование типа возвращаемого имени"""
        bun = Bun("test", 100)
        assert isinstance(bun.get_name(), str)

    def test_bun_price_type(self):
        """Тестирование типа возвращаемой цены"""
        bun = Bun("test", 100.5)
        assert isinstance(bun.get_price(), float)
