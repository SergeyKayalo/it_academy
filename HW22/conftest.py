import os
import pytest
import practice_calculator as calc

# Задание 1.1. Простая фикстура с данными
@pytest.fixture(autouse=False, scope='session')
def book_data():
    return {"title": "1984", "author": "George Orwell", "pages": 328}


# Задание 1.2. Жизненный цикл (Setup / Teardown)
@pytest.fixture(autouse=False, scope='session')
def temp_list():
    a = [1, 2, 3]
    yield a
    a.clear()


# Задание 1.3. Вызов через @pytest.mark.usefixtures
@pytest.fixture(autouse=False, scope='session')
def env_setup():
    os.environ["APP_MODE"] = "testing"
    yield
    del os.environ["APP_MODE"]


# Задание 1.4. Цепочка зависимостей
@pytest.fixture(autouse=False, scope='session')
def base_url():
    return "https://example.com"


@pytest.fixture(autouse=False, scope='session')
def users_endpoint(base_url):
    return f"{base_url}/users"


# Задание 1.5. Параметризация фикстуры (params)
@pytest.fixture(autouse=False, scope='session', params=[2, 4, 6, 8])
def number(request):
    return request.param


# Задание 1.7. Поправьте калькулятор из урока 21
@pytest.fixture(autouse=False, scope='session')
def mycalc():
    return calc.Calculator()



