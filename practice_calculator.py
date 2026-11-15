from dataclasses import dataclass, field


@dataclass
class Calculator:
    history: list = field(default_factory=list)

    def add(self, a, b):
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result

    def subtract(self, a, b):
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result

    def multiply(self, a, b):
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result

    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Деление на ноль невозможно")
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result

    def power(self, base, exponent):
        result = base ** exponent
        self.history.append(f"{base} ** {exponent} = {result}")
        return result

    def percentage(self, number, percent):
        if percent < 0:
            raise ValueError("Процент не может быть отрицательным")
        result = number * percent / 100
        self.history.append(f"{percent}% от {number} = {result}")
        return result

    def clear_history(self):
        self.history.clear()

    def get_history(self):
        return self.history.copy()
