import re

INT_RE   = re.compile(r'^\d+$')
FLOAT_RE = re.compile(r'^\d+\.\d+$')

def parse_number(s):
    s = s.strip()
    if INT_RE.match(s):
        return int(s)
    if FLOAT_RE.match(s):
        return float(s)
    return None

def arithmetic(a, operator, b):
    result = None
    match operator:
        case "+":
            print("Операция сложения")
            result = a + b
        case "-":
            print("Операция вычитания")
            result = a - b
        case "*":
            print("Операция умножения")
            result = a * b
        case "^":
            print("Операция возведения в степень")
            result = a ** b
        case "/":
            print("Операция деления")
            try:
                result = a / b
            except ZeroDivisionError:
                raise ValueError(f"Деление на 0")
        case _:
            raise ValueError(f"Неизвестная операция: {operator!r}")
    return result

def calc():
    a_text = input ("Введите первое число: ")
    a=parse_number(a_text)
    if a is None:
        print("Можно использовать только числа")
        return False
    b_text = input ("Введите второе число: ")
    b=parse_number(b_text)
    if b is None:
        print("Можно использовать только числа")
        return False
    znak = input ("Выберите операцию (Введите +,-,*,^ или /): ")
    # match_znak = ["+","-","*","/","^"]
    # if not znak in match_znak:
    #     print("Не корректная операция!")
    try:
        result = arithmetic(a, znak, b)
    # except ZeroDivisionError as e:
    #     print("Ошибка:", e)
    #     return False
    except ValueError as e:
        print("Ошибка:", e)
        return False
    print(f"{a} {znak} {b} = {result}")
    return True


while True:
    x=int(input("-----------\n1 - Начать расчёт\n0 - Выход\n"))
    if x == 1:
        print("-----------")
        calc()
    else:
        break
print ("Работа завершена")



