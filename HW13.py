import re

print("\nЗадание 1. Генератор только чётных")
def even_numbers(iterable):
    current = iterable
    for number in iterable:
        if number % 2 == 0: yield number

print(list(even_numbers([1, 2, 3, 4, 5, 6])))  # [2, 4, 6]


print("\nЗадание 2. Фильтрация строк по ключевому слову")
def filter_lines(path, keyword: str):
    with open(path, encoding="utf-8") as f:
        for ln in f:
            if keyword.lower() in ln.lower():
                yield ln.strip()

for line in filter_lines("log.txt", "ERROR"):
    print(line)


print("\nЗадание 3. Ленивое соединение двух итерируемых")
def chain(iter1, iter2):
    for item in iter1: yield item
    for item in iter2: yield item

print(list(chain([1, 2], [3, 4])))


print("\nЗадание 4. Бесконечный итератор")
def counter(start=0):
    current = start
    while True:
        yield current
        current += 1

c = counter(10)
print(next(c))  # 10
print(next(c))  # 11
print(next(c))  # 12


print("\nЗадание 5. Ограничение бесконечного генератора")
def take(n, iterable):
    for x in range(n):
        yield next(iterable)

c = counter(100)
print(list(take(5, c)))  # [100, 101, 102, 103, 104]


print("\nЗадание 6. Замена всех пробелов на запятые")
text = "one two three\tfour"
res = re.sub(r"\s",",", text)
print(res)


print("\nЗадание 7. Выделить домены из e‑mail адресов")
emails = ["a@test.com", "b@mail.ru", "user@sub.example.org"]
domains = []
for mail in emails:
    domains += re.findall(r"@.+$", mail)
print(domains)


print("\nЗадание 8. Проверка формата даты")
def is_valid_date(date):
    return re.match(r"\d{4}-\d{2}-\d{2}", date) is not None

assert is_valid_date("2025-12-23")
assert not is_valid_date("25-12-23")


print("\nЗадание 9. Извлечь код ответа из HTTP‑лога")
log = '127.0.0.1 - - "GET /api/v1/users HTTP/1.1" 200 123 "-"'
num = re.search(r'\"GET.+?\"\s(\d+)', log)
print(num.group(1))


print("\nЗадание 10. Валидация пароля")
def is_strong_password(password):
    return re.match(r"^(?=.*[A-Z])(?=.*\d).{8,}$", password) is not None

assert is_strong_password("Abcdef12")
assert not is_strong_password("abcdef12")
assert not is_strong_password("Abcdefgh")


print("\nЗадание 11. Удалить HTML‑теги")
text = "<p>Hello <b>world</b>!</p>"
res = re.sub(r"(<\w+>|</\w+>)","", text)
print(res)


print("\nЗадание 12. Получить все пары ключ=значение")
s = "name=John; age=30; city=London;"
s = re.findall(r"(\w+)=(\w+)", s)
result = {}
for a, b in s:
    result[a] = b
print(result)


print("\nЗадание 13. Вытащить номер телефона")
def find_phones(t):
    return re.findall(r"(\+7\-\d{3}\-\d{3}\-\d{2}\-\d{2}|\d \(\d{3}\) \d{3}-\d{2}-\d{2})", t)

text = "Мой телефон: +7-999-123-45-67, офис: 8 (812) 555-66-77."
print(find_phones(text))


print("\nЗадание 14. Разбить строку по нескольким разделителям")
s = "one,two;three four"
print (re.split(r",|;|\s+", s))


print("\nЗадание 15. Извлечь данные из URL")
s = "/api/v1/users/123/orders/456"
parse = re.findall(r"users/(\d+)/orders/(\d+)", s)
for users, orders in parse:
    print([int(users), int(orders)])



