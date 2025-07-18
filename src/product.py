class Product:
    """Класс для представления продукта"""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, products_data: dict) -> "Product":
        """Создает новый экземпляр Product из словаря данных"""
        return cls(
            name=products_data["name"],
            description=products_data["description"],
            price=products_data["price"],
            quantity=products_data["quantity"]
        )

    @property
    def price(self) -> float:
        """Возвращает цену продукта"""
        return self.__price

    @price.setter
    def price(self, correct_price: float) -> None:
        """Устанавливает новую цену продукта, если она положительная"""
        if correct_price > 0:
            self.__price = correct_price
        else:
            print("Цена не должна быть нулевая или отрицательная")

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."
