import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def first_category():
    return Category(
        name="Смартфоны",
        description=(
            "Смартфоны, как средство не только коммуникации,"
            " но и получения дополнительных функций для удобства жизни"
        ),
        products=[
            Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
            Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
            Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
        ]
    )


@pytest.fixture
def second_category():
    return Category(
        name="Телевизоры",
        description=(
            "Современный телевизор, который позволяет наслаждаться просмотром, "
            "станет вашим другом и помощником"
        ),
        products=[Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)]
    )


def test_first_category(first_category):
    assert first_category.name == "Смартфоны"
    assert first_category.description == (
        "Смартфоны, как средство не только коммуникации, "
        "но и получения дополнительных функций для удобства жизни"
    )

    assert first_category.products[0].name == "Samsung Galaxy S23 Ultra"
    assert first_category.products[0].description == "256GB, Серый цвет, 200MP камера"
    assert first_category.products[0].price == 180000.0
    assert first_category.products[0].quantity == 5

    assert first_category.products[1].name == "Iphone 15"
    assert first_category.products[1].description == "512GB, Gray space"
    assert first_category.products[1].price == 210000.0
    assert first_category.products[1].quantity == 8

    assert first_category.products[2].name == "Xiaomi Redmi Note 11"
    assert first_category.products[2].description == "1024GB, Синий"
    assert first_category.products[2].price == 31000.0
    assert first_category.products[2].quantity == 14


def test_second_category(second_category):
    assert second_category.name == "Телевизоры"
    assert second_category.description == (
        "Современный телевизор, который позволяет наслаждаться просмотром, "
        "станет вашим другом и помощником"
    )

    assert second_category.products[0].name == "55\" QLED 4K"
    assert second_category.products[0].description == "Фоновая подсветка"
    assert second_category.products[0].price == 123000.0
    assert second_category.products[0].quantity == 7
