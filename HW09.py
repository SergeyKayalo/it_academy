# 1.  Красивый вывод объекта теста (__str__, __repr__)
class TestCase:
    def __init__(self, *args):
        self.args = args

    def __str__(self):
        # для пользователя, print()
        ret = ""
        for arg in self.args:
            ret = ret + "|" + str(arg) if ret else str(arg)
        return ret

    def __repr__(self):
        # для разработчика, интерактивка, логирование
        return f"TestCase(args={self.args})"


t = TestCase("test_login", "passed", "что то ещё", "ещё текст")
print(t)
print([t])


# 2.Коллекция тестов с len() и bool()
class TestSuite:
    def __init__(self, tests):
        self.tests = tests

    def __len__(self):
        return len(self.tests)

    def __bool__(self):
        # Suite считается "истинной", если есть хотя бы один тест
        return len(self.tests) > 0


suite = TestSuite(["test_login", "test_signup"])
print(len(suite))  # 2
if suite:
    print("Suite не пустой")


# 3.Результаты тестов как словарь

class Results:
    def __init__(self):
        self.results = {}

    def __getitem__(self, item):
        return self.results[item]

    def __setitem__(self, key, value):
        self.results[key] = value


results = Results()
results["test_login"] = "passed"
print(results["test_login"])


# 4. Итерация по коллекции тестов (__iter__)

class TestSuite:
    def __init__(self, tests):
        self.tests = tests

    def __iter__(self):
        return iter(self.tests)


suite = TestSuite(["test_login", "test_signup"])
for test in suite:
    print(test)


class Duration:
    def __init__(self, ret):
        self.ret = ret

    def __float__(self):
        return float(self.ret)

    def __add__(self, other):
        return float(self.ret + other.ret)


t1 = Duration(1.5)
t2 = Duration(2.3)
print(t1 + t2)  # 3.80 sec


# 6. Объект как функция (__call__)
class TestRunner:
    def __init__(self, tests):
        self.tests = tests

    def __call__(self):
        for name in self.tests:
            print(f"Running {name}...")


runner = TestRunner(["test_login", "test_signup"])
runner()


class Version:
    def __init__(self, major, minor):
        self.major = major
        self.minor = minor

    def __eq__(self, other):
        return (self.major, self.minor) == (other.major, other.minor)

    def __lt__(self, other):
        return (self.major, self.minor) < (other.major, other.minor)



v1 = Version(1, 2)
v2 = Version(1, 3)
print(v1 < v2)  # True
print(v1 == v2)  # False
