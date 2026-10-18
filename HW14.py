from email.mime import image
from pathlib import Path

BASE = Path(__file__).parent

print("\nЗадание 5. Добавить запись в лог")
def log_message(path, message):
    file = BASE / path
    with file.open("a") as f:
        f.writelines(message + "\n")

log_message("app.log", "Test started")
log_message("app.log", "Test finished")




print("\nЗадание 6. Прочитать первые N символов")
def read_first_chars(path, n):
    file = BASE / path
    with file.open("r") as f:
        return f.read(n)

print(read_first_chars("app.log", 20))




print("\nЗадание 7. Фильтрация строк по ключевому слову")
def filter_file(src, dst, keyword):
    file_in = BASE / src
    file_out = BASE / dst
    with file_in.open("r") as f_in, file_out.open("w") as f_out:
        for line in f_in:
            if keyword.lower() in line.lower():
                f_out.write(line)
    return f_out

filter_file("log.txt", "log_errors.log", "ERROR")




print("\nЗадание 8. Подсчитать сумму чисел в файле")
def sum_file(file_path):
    file_in = BASE / file_path
    total = 0
    with file_in.open("r") as f_in:
        for line in f_in:
            try:
                total += int(line.strip())
            except ValueError:
                print(f"{line.strip()} не является числом")
    return total

print(sum_file("numbers.txt"))




print("\nЗадание 9. Работа с бинарным файлом (копия)")
def copy_binary(image_in, image_out):
    file_in = BASE / image_in
    file_out = BASE / image_out
    with file_in.open("br") as f_in, file_out.open("bw") as f_out:
        for line in f_in:
            f_out.write(line)
    return f_out

copy_binary("image.png", "image_copy.png")




print("\n10. Безопасное чтение конфигурации")
def read_config(config_file):

    file_in = BASE / config_file
    config = {}
    with file_in.open("r") as f_in:
        for line in f_in:
            line_list = line.split("=")
            config[line_list[0].strip()] = line_list[1].strip()
    return config

print(read_config("config.txt"))

