print("7.1 Получить инициалы из ФИО")
fullname = "Иванов Иван Иванович"
split_name = fullname.split(" ")
print(split_name[0] + " " + split_name[1][0] + ". " + split_name[2][0] + ".")
print()

print("7.2 Подсчёт количества слов в предложении")
t = "We are python learners"
t_len=len(t.split())
print(t_len)
print()

print("7.3 Инвертирование строки (реверс)")
t = "We are python learners"
print("".join(reversed(t)))
print()

print("7.4 Удаление всех пробелов из строки")
t = "We are python learners"
print(t.replace(" ",""))
print()

print("7.5 Проверка наличия подстроки")
t1 = input() # "We are python learners"
t2 = input() # "python learners"
print (t2 in t1)
print()

print("7.6 Замена всех вхождений символа")
t = input() # "We are python learners"
t1 = input() # "e"
t2 = input() # "*"
print (t.replace(t1,t2))
print()

print("7.7 Проверка, является ли строка числом")
t = input() # "We are python learners"
print (t.isdigit())
