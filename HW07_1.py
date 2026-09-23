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


def calc():
    result = None
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
    match_znak = ["+","-","*","/","^"]
    if not znak in match_znak:
        print("Не корректная операция!")
    match znak:
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
            if b == 0:
                print("На 0 делить нельзя!")
            else:
                result = a / b
    print(f"{a} {znak} {b} = {result}")
    return True


while True:
    calc()


