# Задание 1
n = input("Введите строку:")
for i in n:
    print(i)

# Задание 2
n = input("Введите строку:")
count=0
for i in n:
    if i.lower() in "aeiou": count += 1
print(f"Количество гласных в строке: {count}")

# Задание 3
n = input("Введите несколько тестовых названий (через пробел) :")
for i in n.split():
    print (f"Test Case: {i}")

# Задание 4
n = ""
passwd = "12345"
while n != passwd:
    n = input("Введите пароль :")

# Задание 5
for i in range(11):
    if i % 3 == 0: continue
    print(i)

# Задание 6
summ = 0
for i in range(1,101):
    summ += i
print(summ)

# Задание 7
os = ["Windows", "Linux", "Darwin", "MacOs"]
browsers = ["Mozilla", "Opera", "Safari", "Chrome"]
combo=[]
for browser in browsers:
    for o in os:
        combo.append(browser +' '+ o)
print(combo)

# Задание 8
s = "Это произвольная строка"
for i, itms in enumerate(s):
    print(f"Индекс: {i}, буква: {itms}")

# Задание 9
n = input("Введите строку:")
check = False
for i in n:
    if i == "@":
        check = True
        break
if check:
    print("Есть @")
else:
    print("Нет @")

# Задание 9 вариант 2
n = input("Введите строку:")
if any(i == "@" for i in n):
    print("Есть @")
else:
    print("Нет @")


# Задание 10
d = 10
while d >= 0:
    print(d)
    d -= 1

# Задание 11
s = "Это произвольная строка"
for i in s:
    print(i.upper())

# Задание 12
while True:
    n = input("Введите число:")
    if int(n) > 10: break

# Задание 13
count = 0
n = "пять тестовых слов через пробел"
for i in n.split():
    count += 1
print(count)

# Задание 14
for i in range(1,21):
    print(i)
    if i == 15: break

