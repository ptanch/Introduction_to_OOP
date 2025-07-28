from src.product import Product


class LawnGrass(Product):
    """Подкатегория класса Product для представления Газонная трава"""

    def __init__(
            self,
            name: str,
            description: str,
            price: float,
            quantity: int,
            country: str,
            germination_period: str,
            color: str
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        if type(other) is type(self):
            return super().__add__(other)
        else:
            raise TypeError("Можно складывать только траву с травой")
