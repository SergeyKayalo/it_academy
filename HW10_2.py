from abc import ABC, abstractmethod
import math

print("\n1.1 валидация через setter")
class Product:

    def __init__(self, _price):
        self._price = _price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, _price):
        self._price = _price if _price > 0 else self._price


p = Product(100)
print(p.price)
p.price = 250
print(p.price)
p.price = -10
print(p.price)




print("\n1.2 Вычисляемое свойство")
class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def area(self):
        return self._width * self._height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

rect = Rectangle(3, 4)
print(rect.area)
rect.width = 10
print(rect.area)




print("\n1.3. Свойство для процента выполнения тестов")
class TestStats:
    def __init__(self, passed, total):
        self._passed = passed
        self._total = total

    @property
    def success_rate(self):
        return f"{self._passed / self._total * 100:.1f}"

    @property
    def passed(self):
        return self._passed

    @property
    def total(self):
        return self._total

    @passed.setter
    def passed(self, value):
        self._passed = value

    @total.setter
    def total(self, value):
        self._total = value

stats = TestStats(8, 10)
print(stats.success_rate)  # 80.0
stats.passed = 9
print(stats.success_rate)  # 90.0




print("\n2.1. Миксин для проверки прав")
class PermissionMixin:
    def has_permission(self, user_role):
        return True if user_role == 'admin' else False

class SecureAction(PermissionMixin):

    def execute(self, user_role):
       if self.has_permission(user_role):
           print ("Админ. Метод запущен")
       else:
           print("Нет прав")

action = SecureAction()
action.execute("user") # Нет прав.
action.execute("admin") # Админ. Метод запущен




print("\n2.2 Делегирование логгеру")
class Logger:
    def log(self, string=""):
        print(f"[LOG]{string}")


class Service:
    def __init__(self, logger = Logger()):
        self.logger = logger

    def process(self):
        self.logger.log("Начало обработки")
        print("Обработка данных")
        self.logger.log("Закончил обработку")


s = Service()
s.process()




print("\n2.3. Разные роли пользователя")
class Admin:
    def create_user(self, username):
        self.username = username
        print ("Create User: " + username)


class Support:
    def create_ticket(self, title):
        self.title = title
        print ("Create Ticket: " + title)


class SuperUser(Admin, Support):
    pass


su = SuperUser()
su.create_user("Ivan")
su.create_ticket("Падает сервис")




print("\n2.4. Порядок разрешения методов (MRO)")
class A:
    def who_am_i(self):
        print ("А")

class B(A):
    def who_am_i(self):
        print ("B")

class C(A):
    def who_am_i(self):
        print ("C")

class D(B,C):
    pass

d = D()
d.who_am_i()       # B (по MRO)
print(D.mro())




print("\n2.5. Несколько миксинов")
class LoggingMixin:
    def log(self, message=""):
        print(f"[LOG]{message}")


class RetryMixin:

    def retry(self, count):
        for i in range(1, count+1):
            print(f"Попытка {i}")
            self.log("Выполняем задачу")
            self.run()

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def log(self, message):
        pass


class Job(LoggingMixin, RetryMixin):
    def run(self):
        print("Job что-то делает...")


j = Job()
j.retry(2)





print("\n3.1. Базовый абстрактный класс «Фигура»")
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return f"Прямоугольник. Площадь: {self.width * self.height} см²"


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return f"Круг. Площадь: {self.radius ** 2 * math.pi:.2f} см²"


shapes = [Rectangle(3, 4), Circle(2)]
for s in shapes:
    print(s.area())




print("\n3.2. Абстракция «Транспорт» с шаблонным методом")
class Transport:
    def move(self):
        pass

    def go(self):
        print ("Начинаем движение")
        self.move()


class Car(Transport):
    def move(self):
        print("Едем по дороге на машине")


class Bike(Transport):
    def move(self):
        print("Едем на велосипеде")


for t in (Car(), Bike()):
    t.go()




print("\n3.3. Абстракция для автотестов: BaseTestCase")
class BaseTestCase(ABC):

    @abstractmethod
    def prepare_data(self):
        pass

    @abstractmethod
    def run_test(self):
        pass

    def run(self):
        print (self.__doc__)
        self.prepare_data()
        self.run_test()


class LoginTest(BaseTestCase):
    """=== LoginTest ==="""
    def prepare_data(self):
        print ("Готовим пользователя для логина")

    def run_test(self):
        print("Проверяем успешный логин")


class PaymentTest(BaseTestCase):
    """=== PaymentTest ==="""
    def prepare_data(self):
        print ("Готовим данные карты и баланс")

    def run_test(self):
        print("Проверяем успешный платеж")


tests = [LoginTest(), PaymentTest()]
for t in tests:
    t.run()




print("\n4.1. Полиморфные тесты (API и UI)")
class BaseTest(ABC):
    def __init__(self,test_name):
        self.test_name = test_name

    @abstractmethod
    def run(self):
        pass

class APITest(BaseTest):
    def run(self):
        print(f"API тест: проверяем эндпоинт {self.test_name}")

class UITest(BaseTest):
    def run(self):
        print(f"UI тест: проверяем страницу {self.test_name}")

def run_all(tests):
    for test in tests:
        test.run()

tests = [
    APITest("/login"),
    UITest("LoginPage"),
    APITest("/users"),
]
run_all(tests)




print("\n4.2. Полиморфизм через утиный тип (без ABC)")
class TestCollection:

    def __init__(self, collection):
        self.collection = collection

    def __len__(self):
        return len(self.collection)


def print_length(obj):
    t = TestCollection(obj)
    print(len(t))

print_length("Python")  # 6
print_length([1, 2, 3])  # 3
print_length({"a": 1, "b": 2})  # 2
print_length(TestCollection([10, 20, 30, 40]))  # 4
