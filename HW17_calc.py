import argparse
import re
from pathlib import Path

INT_RE   = re.compile(r'^-?\d+$')
FLOAT_RE = re.compile(r'^-?\d+\.\d+$')
args = None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=f"Консольный калькулятор.",
                                    epilog = f" Пример использования: {Path(__file__).name} 10 '+' 2",
                                    exit_on_error = True)
    # Позиционные
    parser.add_argument("a_text", help="Первое число")
    parser.add_argument("znak", choices=["+", "-", "*", "/", "^"], help="Арифмитический знак")
    parser.add_argument("b_text", help="Второе число")
    args = parser.parse_args()

def parse_number(s):
    s = re.sub(r"\s+", "", s)
    if INT_RE.match(s):
        return int(s)
    if FLOAT_RE.match(s):
        return float(s)
    return None

def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def power (a, b):
    return a ** b


def arithmetic(a, operator, b):
    result = None
    match operator:
        case "+":
            print(f"Операция сложения: {a} + {b}")
            result = plus(a, b)
        case "-":
            print(f"Операция вычитания: {a} - {b}")
            result = minus(a, b)
        case "*":
            print(f"Операция умножения: {a} * {b}")
            result = multiply(a, b)
        case "^":
            print(f"Операция возведения в степень: {a} ** {b}")
            try:
                result = power(a, b)
            except ZeroDivisionError:
                raise ValueError(f"Возведение в отрицательную степень {b} числа с основанием {a}")
            except OverflowError:
                raise ValueError(f"Переполнение при возведении в степень: {a} ^ {b}")
        case "/":
            print(f"Операция деления: {a} / {b}")
            try:
                result = divide(a, b)
            except ZeroDivisionError:
                raise ValueError(f"Деление на 0")
        case _:
            raise ValueError(f"Неизвестная операция: {operator!r}")
    return result

def calc():
    a=parse_number(args.a_text)

    if a is None:
        print(a)
        print("Можно использовать только числа")
        return False
    b=parse_number(args.b_text)
    if b is None:
        print(b)
        print("Можно использовать только числа")
        return False
    try:
        result = arithmetic(a, args.znak, b)
    except ValueError as e:
        print("\033[31mОшибка\033[0m:", e)
        return False
    print(f"{a} {args.znak} {b} = {result}")
    return True

if args:
    calc()

print ("Работа завершена")



