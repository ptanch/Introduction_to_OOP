import pytest

from src.category import Category
from src.lawn_grass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


# === Products ===
@pytest.fixture
def first_product():
    return Product(
        name="Samsung Galaxy S23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5
    )


@pytest.fixture
def second_product():
    return Product(
        name="Iphone 15",
        description="512GB, Gray space",
        price=210000.0,
        quantity=8
    )


@pytest.fixture
def third_product():
    return Product(
        name="Xiaomi Redmi Note 11",
        description="1024GB, Синий",
        price=31000.0,
        quantity=14
    )


@pytest.fixture
def fourth_product():
    return Product(
        name="55\" QLED 4K",
        description="Фоновая подсветка",
        price=123000.0,
        quantity=7
    )


# === Category ===
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


# === Smartphones ===
@pytest.fixture
def smartphone1():
    return Smartphone(
        name="Samsung Galaxy S23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5,
        efficiency=95.5,
        model="S23 Ultra",
        memory=256,
        color="Серый"
    )


@pytest.fixture
def smartphone2():
    return Smartphone(
        name="Iphone 15",
        description="512GB, Gray space",
        price=210000.0,
        quantity=8,
        efficiency=98.2,
        model="15",
        memory=512,
        color="Gray space"
    )


# === Grass ===
@pytest.fixture
def grass1():
    return LawnGrass(
        name="Газонная трава",
        description="Элитная трава для газона",
        price=500.0,
        quantity=20,
        country="Россия",
        germination_period="7 дней",
        color="Зеленый"
    )


@pytest.fixture
def grass2():
    return LawnGrass(
        name="Газонная трава 2",
        description="Выносливая трава",
        price=450.0,
        quantity=15,
        country="США",
        germination_period="5 дней",
        color="Темно-зеленый"
    )
