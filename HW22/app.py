import random
import time


# Задание 2.1: Мок времени (time.sleep)
def process_files():
    print("Обработка файлов...")
    time.sleep(3)  # Замедляет тест!
    print("Готово!")
    return "processed"


# Задание 2.2: Мок чтения файла (open)
def read_config(filename):
    with open(filename, 'r') as f:
        return f.read().strip()


# Задание 2.3: Мок случайных чисел (random)
def generate_password(length=8):
    chars = "abc123"
    return ''.join(random.choice(chars) for i in range(length))
