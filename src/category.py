from src.product import Product


class Category:
    """Класс для представления категории"""

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Product]):
        self.name = name
        self.description = description
        self.__products = products

        # Увеличиваем общее количество категорий при создании нового объекта
        Category.category_count += 1

        # Прибавляем количество товаров в этой категории
        Category.product_count += len(products)

    def add_product(self, product: Product) -> None:
        """Добавление товаров в категорию"""
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError

    @property
    def products(self) -> str:
        """Вывод списка товаров в виде строк"""
        return ''.join(str(product) + '\n' for product in self.__products)

    @property
    def product_items(self) -> list[Product]:
        """Возвращает список объектов продуктов в категории"""
        return self.__products

    def __str__(self) -> str:
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."
