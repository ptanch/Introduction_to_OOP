import pytest

from src.product import Product


#  Тест с инициализацией первого продукта
def test_init_first(first_product):
    assert first_product.name == "Samsung Galaxy S23 Ultra"
    assert first_product.description == "256GB, Серый цвет, 200MP камера"
    assert first_product.price == 180000.0
    assert first_product.quantity == 5


#  Тест с инициализацией второго продукта
def test_init_second(second_product):
    assert second_product.name == "Iphone 15"
    assert second_product.description == "512GB, Gray space"
    assert second_product.price == 210000.0
    assert second_product.quantity == 8


#  Тест с инициализацией третьего продукта
def test_init_third(third_product):
    assert third_product.name == "Xiaomi Redmi Note 11"
    assert third_product.description == "1024GB, Синий"
    assert third_product.price == 31000.0
    assert third_product.quantity == 14


#  Тестирование класс-метода
def test_new_product_from_dict():
    data = {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5
    }

    product = Product.new_product(data)

    assert isinstance(product, Product)
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


#  Тест для геттера
def test_price_property(first_product, second_product, third_product, fourth_product):
    assert first_product.price == 180000.0
    assert second_product.price == 210000.0
    assert third_product.price == 31000.0
    assert fourth_product.price == 123000.0


#  Тесты для сеттера
def test_price_setter_valid():
    product = Product("Smartphone", "Test product", 100.0, 2)
    product.price = 800.0
    assert product.price == 800.0


def test_price_setter_invalid(capsys):
    product = Product("Smartphone", "Test product", 100.0, 2)
    product.price = -100.0  # попытка задать недопустимую цену
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-1] == "Цена не должна быть нулевая или отрицательная"
    assert product.price == 100.0  # значение не изменилось


def test_product_str(first_product):
    expected_str = "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."
    assert str(first_product) == expected_str


def test_product_add(first_product, second_product):
    # (180000 * 5) + (210000 * 8) = 900000 + 1680000 = 2580000.0
    expected_sum = 2580000.0
    result = first_product + second_product
    assert result == expected_sum


def test_product_add_with_non_product(first_product):
    with pytest.raises(TypeError):
        _ = first_product + 10
