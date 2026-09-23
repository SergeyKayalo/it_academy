# Задание 2.1
test_results = [
    {"name": "login_test", "status": "passed", "duration": 2.1},
    {"name": "payment_test", "status": "failed", "duration": 3.5},
    {"name": "logout_test", "status": "passed", "duration": 1.2}
]
result = filter(lambda x:x["status"]=="passed",test_results)
print("Успешные тесты: ", [y["name"] for y in result])

# Задание 2.2
tests = [
    {"name": "complex_test", "duration": 5.2},
    {"name": "simple_test", "duration": 1.1},
    {"name": "medium_test", "duration": 3.4}
]
tests.sort(key = lambda x:x["duration"])
print(tests)

# Задание 2.3
emails = ["test@gmail.com", "invalid-email", "user@company.ru", "no@domain"]
result = filter(lambda x:"@" in x and (x.endswith(".com") or x.endswith(".ru")),emails)
print(list(result))