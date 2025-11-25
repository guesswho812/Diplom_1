import pytest


class TestBun:
    """Тесты для класса Bun"""
    
    def test_bun_initialization(self, bun):
        """Только инициализация"""
        assert bun.name == "Краторная булочка"
        assert bun.price == 100.0
    
    def test_bun_get_name(self, bun):
        """Только получение названия"""
        assert bun.get_name() == "Краторная булочка"
    
    def test_bun_get_price(self, bun):
        """Только получение цены"""
        assert bun.get_price() == 100.0
    
    @pytest.mark.parametrize("name, price", [
        ("Булочка 1", 50.0),
        ("Булочка 2", 150.5), 
        ("С кунжутом", 75.25),
    ])
    def test_bun_different_parameters(self, name, price):
        """Тестируем разные параметры"""
        from bun import Bun
        bun = Bun(name, price)
        assert bun.get_name() == name
        assert bun.get_price() == price