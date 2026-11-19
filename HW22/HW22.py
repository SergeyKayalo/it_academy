import pytest
import os
from app import process_files, read_config, generate_password
# фикстуры в conftest.py

# Задание 1.1. Простая фикстура с данными
def test_book_pages(book_data):
    assert book_data["pages"] > 300


# Задание 1.2. Жизненный цикл (Setup / Teardown)
def test_list(temp_list):
    temp_list.append(4)
    assert len(temp_list) == 4


# Задание 1.3. Вызов через @pytest.mark.usefixtures
@pytest.mark.usefixtures("env_setup")
def test_app_mode():
    assert os.environ["APP_MODE"] == "testing"


# Задание 1.4. Цепочка зависимостей
def test_url(users_endpoint):
    assert users_endpoint == "https://example.com/users"


# Задание 1.5. Параметризация фикстуры (params)
def test_is_even(number):
    assert number % 2 == 0


# Задание 1.6. Встроенная фикстура tmp_path
def test_path_tmp(tmp_path ):
    tmp_path.mkdir(exist_ok=True)
    file = tmp_path / "hello.txt"
    file.write_text("Pytest is awesome")
    assert file.exists() and file.read_text() == "Pytest is awesome"


# Задание 2.1: Мок времени (time.sleep)
def test_process_files(mocker):
    mock_time=mocker.patch("app.time.sleep")
    func = process_files()
    mock_time.assert_called_once_with(3)
    assert func == "processed"


# Задание 2.2: Мок чтения файла (open)
def test_read_config(mocker):
    read_filename = "config.txt"
    mock_file = mocker.mock_open(read_data="host=localhost")
    mocker.patch("builtins.open", mock_file)
    func = read_config(read_filename)
    mock_file.assert_called_once_with(read_filename, "r")
    assert func == "host=localhost"


# Задание 2.3: Мок случайных чисел (random)
def test_generate_password(mocker):
    return_password = "aaaabbbb"
    mock_choice = mocker.patch("app.random.choice")
    mock_choice.side_effect = list(return_password)
    func = generate_password()
    mock_choice.assert_called_with("abc123")
    assert func == return_password
