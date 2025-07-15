from src.category import Category


def test_first_category(first_category):
    assert first_category.name == "Смартфоны"
    assert first_category.description == (
        "Смартфоны, как средство не только коммуникации, "
        "но и получения дополнительных функций для удобства жизни"
    )

    assert first_category.product_items[0].name == "Samsung Galaxy S23 Ultra"
    assert first_category.product_items[0].description == "256GB, Серый цвет, 200MP камера"
    assert first_category.product_items[0].price == 180000.0
    assert first_category.product_items[0].quantity == 5

    assert first_category.product_items[1].name == "Iphone 15"
    assert first_category.product_items[1].description == "512GB, Gray space"
    assert first_category.product_items[1].price == 210000.0
    assert first_category.product_items[1].quantity == 8

    assert first_category.product_items[2].name == "Xiaomi Redmi Note 11"
    assert first_category.product_items[2].description == "1024GB, Синий"
    assert first_category.product_items[2].price == 31000.0
    assert first_category.product_items[2].quantity == 14


def test_second_category(second_category):
    assert second_category.name == "Телевизоры"
    assert second_category.description == (
        "Современный телевизор, который позволяет наслаждаться просмотром, "
        "станет вашим другом и помощником"
    )

    assert second_category.product_items[0].name == "55\" QLED 4K"
    assert second_category.product_items[0].description == "Фоновая подсветка"
    assert second_category.product_items[0].price == 123000.0
    assert second_category.product_items[0].quantity == 7


def test_category_class_counters(first_product, second_product, third_product, fourth_product):
    Category.category_count = 0
    Category.product_count = 0

    Category('Smartphone', '', products=[first_product, second_product, third_product])
    Category('TV', '', products=[fourth_product])

    assert Category.category_count == 2
    assert Category.product_count == 4


def test_add_product(first_category, fourth_product):
    initial_count = len(first_category.product_items)
    initial_total = Category.product_count

    first_category.add_product(fourth_product)

    assert len(first_category.product_items) == initial_count + 1
    assert Category.product_count == initial_total + 1
    assert first_category.product_items[-1] == fourth_product


def test_product_property(first_category, second_category):
    expected_output_first = (
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
        "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n"
    )

    expected_output_second = (
        "55\" QLED 4K, 123000.0 руб. Остаток: 7 шт.\n"
    )

    assert first_category.products == expected_output_first
    assert second_category.products == expected_output_second
