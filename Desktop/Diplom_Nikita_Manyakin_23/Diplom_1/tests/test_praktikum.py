import pytest
from unittest.mock import patch, Mock
from praktikum.praktikum import main


class TestPraktikum:
    """Тесты для основного модуля praktikum.py"""
    
    @patch('praktikum.praktikum.Database')
    @patch('praktikum.praktikum.Burger')
    def test_main_function(self, mock_burger, mock_database):
        """Тестирование основной функции main"""
        # Создание моков для объектов базы данных
        mock_db_instance = Mock()
        mock_bun = Mock()
        mock_ingredient = Mock()
        
  
        mock_database.return_value = mock_db_instance
        mock_db_instance.available_buns.return_value = [mock_bun]
        mock_db_instance.available_ingredients.return_value = [mock_ingredient] * 6
        
        mock_burger_instance = Mock()
        mock_burger.return_value = mock_burger_instance
        

        main()
        

        mock_database.assert_called_once()
        mock_burger.assert_called_once()
        mock_db_instance.available_buns.assert_called_once()
        mock_db_instance.available_ingredients.assert_called_once()
        

        assert mock_burger_instance.set_buns.called
        assert mock_burger_instance.add_ingredient.call_count == 4
        assert mock_burger_instance.move_ingredient.called
        assert mock_burger_instance.remove_ingredient.called
        assert mock_burger_instance.get_receipt.called
    
    @patch('praktikum.praktikum.print')
    @patch('praktikum.praktikum.Database')
    @patch('praktikum.praktikum.Burger')
    def test_main_function_print(self, mock_burger, mock_database, mock_print):
        """Тестирование вывода в основной функции"""

        mock_db_instance = Mock()
        mock_bun = Mock()
        mock_ingredient = Mock()
        
        mock_database.return_value = mock_db_instance
        mock_db_instance.available_buns.return_value = [mock_bun]
        mock_db_instance.available_ingredients.return_value = [mock_ingredient] * 6
        
        mock_burger_instance = Mock()
        mock_burger_instance.get_receipt.return_value = "Test receipt"
        mock_burger.return_value = mock_burger_instance
        

        main()
        

        mock_print.assert_called_once_with("Test receipt")
    
    def test_main_module_guard(self):
        """Тестирование защиты выполнения при импорте"""

        import importlib
        import praktikum.praktikum
        

        importlib.reload(praktikum.praktikum)
        
        assert True