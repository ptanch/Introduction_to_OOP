# Приложение Магазин: Категории и Товары

## Проект на Python, в котором реализованы классы для представления категорий товаров (`Category`) и самих товаров (`Product`). Также в проекте присутствуют автотесты, проверяющие корректную работу логики функций.

## Установка
### Требования

+ Python 3.10 или выше (проект проверен на 3.13)
+ pip / poetry
+ Git (для клонирования)

### Установка с помощью `poetry`
```
git clone https://github.com/yourusername/bank-transactions-analyzer.git
cd bank-transactions-analyzer
poetry install
```

#### Если `poetry` не установлен:
```
pip install poetry
```

## Структура проекта
```
project/
│
├── src/
│ ├── category.py # Класс Category
│ ├── lawn_grass.py # Класс LawnGrass (подкласс Product)
│ ├── smartphone.py # Класс Smartphone (подкласс Product)
│ └── product.py # Класс Product
│
├── tests/
│ ├── conftest.py # Фикстуры
│ ├── test_product.py # Тесты на Product
│ ├── test_lawn_grass.py # Тесты на LawnGrass
│ ├── test_smartphone.py # Тесты на Smartphone
│ └── test_category.py # Тесты на Category и Product
│
├── main.py # Пример использования классов
├── .gitignore # Определения игнорируемых файлов и каталогов
└── README.md # Описание проекта
```
### Запуск программы
```poetry run python main.py```

## Описание классов
### `Product`
Класс для представления товара.

**Поля:**
- `name` — название товара
- `description` — описание товара
- `price` — цена
- `quantity` — количество на складе

### `Category`
Класс для представления категории товаров.

**Поля:**
- `name` — название категории
- `description` — описание категории
- `products` — список товаров в категории

## Описание классов-наследников

### `LawnGrass(Product)`
Подкласс для представления продукта "Трава"

**Поля: основные поля наследуются от класса Product**
- `country` — название страны-производителя
- `germination_period` — срок прорастания
- `color` — цвет продукта

### `Smartphones(Product)`
Подкласс для представления продукта "Смартфоны"

**Поля: основные поля наследуются от класса Product**
- `efficiency` — производительность продукта
- `model` — модель
- `memory` — объем встроенной памяти
- `color` — цвет продукта

**Атрибуты класса:**
- `category_count` — общее количество созданных категорий
- `product_count` — общее количество всех товаров во всех категориях

**Методы классов:**

Category
- Метод `add_product` - добавляет товары в категорию
- Метод `products` - выводит список товаров в виде строк
- Метод `product_items` - возвращает список объектов продуктов в категории

Product
- Метод `new_product` - создает новый экземпляр Product из словаря данных
- Метод-сеттер `price` - возвращает цену продукта
- Метод-геттер `price` - устанавливает новую цену продукта, если она положительная
- Магический метод `__str__` - представление информации в строковом виде
- Магический метод `__add__` - сложение числовых значений продуктов

## Тестирование
Для запуска тестов используется `pytest`

## Примеры использования
```
from src.product import Product
from src.category import Category

phone = Product("iPhone 15", "512GB, Gray space", 210000.0, 8)

category = Category(
    name="Смартфоны",
    description="Современные устройства для жизни",
    products=[phone]
)

print(Category.category_count)  # 1
print(Category.product_count)   # 1
print(category.products[0].name)  # iPhone 15
```
### Обратная связь
Если вы нашли баг или хотите предложить улучшения — создайте issue или pull request.
