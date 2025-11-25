import pytest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.fixture
def ingredient():
    """Фикстура для создания ингредиента"""
    return Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100.0)


class TestIngredient:
    """Тесты для класса Ingredient"""
    
    def test_ingredient_initialization(self, ingredient):
        """Только инициализация"""
        assert ingredient.type == INGREDIENT_TYPE_SAUCE
        assert ingredient.name == "hot sauce"
        assert ingredient.price == 100.0
    
    def test_ingredient_getters(self, ingredient):
        """Только геттеры"""
        assert ingredient.get_type() == INGREDIENT_TYPE_SAUCE
        assert ingredient.get_name() == "hot sauce"
        assert ingredient.get_price() == 100.0
    
    @pytest.mark.parametrize("ingredient_type,name,price", [
        (INGREDIENT_TYPE_SAUCE, "chili sauce", 200.0),
        (INGREDIENT_TYPE_FILLING, "dinosaur", 300.0),
        (INGREDIENT_TYPE_SAUCE, "sour cream", 250.5),
    ])
    def test_ingredient_different_parameters(self, ingredient_type, name, price):
        """Тестируем разные параметры"""
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type
        assert ingredient.get_name() == name
        assert ingredient.get_price() == price