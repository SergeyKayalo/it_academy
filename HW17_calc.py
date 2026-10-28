import argparse
import re
from pathlib import Path

INT_RE   = re.compile(r'^\d+$')
FLOAT_RE = re.compile(r'^\d+\.\d+$')
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
    s = s.strip()
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
            print("Операция сложения")
            result = plus(a, b)
        case "-":
            print("Операция вычитания")
            result = minus(a, b)
        case "*":
            print("Операция умножения")
            result = multiply(a, b)
        case "^":
            print("Операция возведения в степень")
            result = power(a, b)
        case "/":
            print("Операция деления")
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
        print("Можно использовать только числа")
        return False
    b=parse_number(args.b_text)
    if b is None:
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



