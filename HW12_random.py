import random

#1
n = random.randint(1, 6)
print("Бросок кубика: ",n)

#2
str="abcdefghijklmnopqrstuvwxyz"
str+=str.upper()
password = "".join(random.choices(str, k=8))
print("Случайный пароль из 8 букв: ", password)

#3
tests = ["GET", "POST", "PUT", "DELETE"]
test = random.choice(tests)
print ("Случайный тест-кейс: ", test)

#4
tests = ["test_login", "test_logout", "test_add_to_cart", "test_checkout"]
test = random.choices(tests, k=len(tests))
print ("Случайный порядок тестов: ", test)

#5
users = ["alice", "bob", "carol", "dave", "erin"]
test = random.choices(tests, k=2)
print ("2 случайных пользователя: ", test)

#6
def run_flaky_test():
    if random.random() < 0.3:
        return "FAILED"
    return "PASSED"
print("Симуляция флейки-теста: ", run_flaky_test())

#7
print ("Лотерея из чисел 1-49: ", random.sample(range(1, 50), 6))

#8
def generate_test_data(n):
    return random.choices(range(1, 101), k=n)
print ("Случайный тестовый набор данных из 10 чисел: ", generate_test_data(10))
print ("Случайный тестовый набор данных из 8 чисел: ", generate_test_data(8))
print ("Случайный тестовый набор данных из 12 чисел: ", generate_test_data(12))



