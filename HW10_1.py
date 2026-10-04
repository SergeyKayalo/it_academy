# 1. Транспорт
class Vehicle:

    def __init__(self, speed):
        self.speed = speed

    def move(self):
        print(f"Двигаюсь со скоростью {self.speed}")


class Car(Vehicle):

    def __init__(self, speed):
        Vehicle.__init__(self, speed)

    def honk(self):
        print("БИП-БИП!")


car = Car(100)
car.move()
car.honk()



# 2.Сотрудники
class Employee:
    def __init__(self, name, salary = 0):
        self.name = name
        self.salary = salary

class Developer(Employee):
    def __init__(self, name, salary = 1000):
        Employee.__init__(self, name, salary)
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary= 2000):
        Employee.__init__(self, name, salary)
        self.salary = salary

manager = Manager("Иван")
print(manager.salary)

developer = Developer("Петя")
print(developer.salary)

# 3. Фигуры
class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y

class Rectangle(Shape):
    def __init__(self, x, y):
        Shape.__init__(self, x, y)
        self.x = x
        self.y = y

class Circle(Shape):
    def __init__(self, x, y):
        Shape.__init__(self, x, y)
        self.x = x
        self.y = y

rect = Rectangle(5, 3)
print(rect.area())

circ = Circle(5, 4)
print(circ.area())

# 4. Банк
class Account:

    def __init__(self, balance = 0):
        self.balance = balance

    def deposit(self,deposit):
        self.balance += deposit
        print(f"К балансу добавили {deposit} BYN. Текущий баланс {self.balance} BYN")

    def withdraw(self, withdraw):
        self.balance -= withdraw
        print(f"C баланса сняли {withdraw} BYN. Текущий баланс {self.balance} BYN")


class SavingsAccount(Account):
    def __init__(self, balance):
        Account.__init__(self, balance)
        self.balance = balance

    def add_interest(self, percent_add = 5):
        percent = (self.balance / 100) * percent_add
        self.balance += percent
        print(f"Произведено начисление {percent_add} процентов. Текущий баланс {self.balance} BYN")


account = SavingsAccount(1000)
account.deposit(600)
account.withdraw(100)
account.add_interest()
print(account.balance)





