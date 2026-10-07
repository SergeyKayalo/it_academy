from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional

print("\n1. Декоратор, добавляющий метаданные тесту")
def test_info(author, component):
    def decorator(cls):
        cls.author = author
        cls.component = component
        return cls
    return decorator


@test_info(author="Иван", component="Auth")
class TestLogin:
    pass


print(TestLogin.author)     # Иван
print(TestLogin.component)  # Auth



print("\n2. Декоратор‑регистратор Page Object’ов")
PAGES = []

def register_page(cls):
    PAGES.append(cls)
    return cls


@register_page
class LoginPage:
    pass

@register_page
class DashboardPage:
    pass

print([cls.__name__ for cls in PAGES])  # ['LoginPage', 'DashboardPage']



print("\n3. Class-based декоратор для добавления тэга")
class Tag:
    def __init__(self, tag):
        self.tag = tag

    def __call__(self, cls):
        cls.tag = self.tag
        return cls

@Tag("smoke")
class SmokeTests:
    pass

@Tag("regression")
class RegressionTests:
    pass


print(SmokeTests.tag)       # smoke
print(RegressionTests.tag)  # regression




print("\n4. Enum окружений и маппинг на URL")


class Environment(Enum):
    DEV = "https://dev.example.com"
    STAGE = "https://stage.example.com"
    PROD = "https://example.com"

def get_base_url(environment):
    return environment.value

# Проверка
print (Environment.DEV)
print(get_base_url(Environment.DEV)) # https://dev.example.com
print(get_base_url(Environment.PROD)) # https://prod.example.com



print("\n5. Enum приоритета и сортировка задач")

class Priority(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3

tasks = [
    ("Починить тест логина", Priority.HIGH),
    ("Обновить документацию", Priority.LOW),
    ("Настроить CI", Priority.MEDIUM),
]

# Сортировка по значению enum
tasks_sorted = sorted(tasks, key=lambda p: p[1].value)

print(tasks_sorted)
for name, prio in tasks_sorted:
    print(prio.name, "-", name)


print("\n7. Парсер числа из строки")
raw = ["10", "20", "abc", "30", "4.5", "40"]
def parse_int_list(list_in):
    new_list = []
    for item in list_in:
        try:
            int(item)
            new_list.append(item)
        except ValueError:
            print(f"{item} не целое число")
    return new_list


nums = parse_int_list(raw)
print(nums)  # [10, 20, 30, 40]



print("\n9. Точка на плоскости")



@dataclass
class Point:
    x: float
    y: float

p1 = Point(1.0, 2.0)
p2 = Point(-3.5, 4.2)

print(p1)  # Point(x=1.0, y=2.0)
print(p2)  # Point(x=-3.5, y=4.2)



print("\n10. Товар и общая стоимость")
@dataclass
class Product:
   name: str
   price: float
   count: int = 1
   def total(self):
       return self.price * self.count

p1 = Product("Keyboard", 50.0, 2)
p2 = Product("Mouse", 25.0)

print(p1, "total:", p1.total())  # 100.0
print(p2, "total:", p2.total())  # 25.0





print("\n11. Книга и авторы")
@dataclass
class Book:
    name: str
    authors: List[str] = field(default_factory=list)
    year: Optional[int] = None
    def formatted(self):
        authors = ", ".join(self.authors) if self.authors else "автор неизвестен"
        year = self.year if self.year is not None else "год неизвестен"
        return f"{self.name} ({year}) - {authors}"


b1 = Book("Python 101", ["John Doe"], 2020)
b2 = Book("Безымянная книга")
b3 = Book("Совместный труд", ["Alice", "Bob"])

for b in (b1, b2, b3):
    print(b.formatted())


