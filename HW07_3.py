# 3.1. Применение проверки к результатам тестов
def apply_test_check(check_func, test_results):
    passed_count=len(list(filter(check_func, test_results)))
    return passed_count

test_results = [
    {"status": "passed"}, {"status": "failed"}, {"status": "passed"}
]

result = apply_test_check(lambda a : a["status"] == "passed", test_results)
print(f"Прошло тестов: {result}")

# 3.2. Фильтрация логов
def filter_logs(logs, filter_func):
    return [log for log in logs if filter_func(log)]

logs = [
    {"level": "INFO", "message": "Test started"},
    {"level": "ERROR", "message": "Login failed"},
    {"level": "WARNING", "message": "Timeout occurred"}
]

error_logs = filter_logs(logs, lambda l: l["level"] == "ERROR")
print("Ошибки:", error_logs)

# 3.3. Трансформация данных тестов (Полноценный пример)
def transform_tests(tests, transform_func):
    return [transform_func(test) for test in tests]

tests = [{"name": "test1", "duration": 2.0}, {"name": "test2", "duration": 3.0}]
increased_tests = transform_tests(tests, lambda t: {**t, "duration": t["duration"] * 1.1})
print("Тесты с увеличенным временем:", increased_tests)

# 4.1. Генератор отчетов
def generate_report(title, *test_names, format="html", **options):
    print("Отчёт: ",title)
    print("Формат: ",format)
    print("Тесты: ", ", ".join(test_names))
    print("author: ", options["author"])


generate_report("Daily Report", "test1", "test2", "test3", format="pdf", author="Tester")


