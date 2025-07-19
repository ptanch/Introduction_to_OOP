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
        self.__products.append(product)
        Category.product_count += 1

    @property
    def product(self) -> str:
        """Вывод категории и количества товаров в виде строк"""
        return ''.join(
            f"{self.name}, количество продуктов: {product.quantity} шт.\n"
            for product in self.__products
        )

    @property
    def product_items(self) -> list[Product]:
        """Возвращает список объектов продуктов в категории"""
        return self.__products
