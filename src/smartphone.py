from src.product import Product


class Smartphone(Product):
    """Подкатегория класса Product для представления Смартфонов"""

    def __init__(
            self,
            name: str,
            description: str,
            price: float,
            quantity: int,
            efficiency: float,
            model: str,
            memory: int,
            color: str
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        if type(other) is type(self):
            return super().__add__(other)
        else:
            raise TypeError("Можно складывать только смартфоны со смартфонами")
