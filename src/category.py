from src.product import Product


class Category:
    """Класс для представления категории"""

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Product]):
        self.name = name
        self.description = description
        self.products = products

        # Увеличиваем общее количество категорий при создании нового объекта
        Category.category_count += 1

        # Прибавляем количество товаров в этой категории
        Category.product_count += len(products)
