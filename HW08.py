import time
import random
import inspect
from functools import wraps

print ("1.	Декоратор повторного запуска тест")
def retry(times):
    print(f"Количество попыток: {times}")
    def decorator(func):
        def wrapper():
            counter = 0
            while counter < times:
                # добавил задержку для наглядности вывода, иначе вывод для всего цикла FAILURE или PASSED
                time.sleep(random.uniform(.1, .2))
                ret=func()
                counter += 1
                if ret != "FAILURE":
                    print(f"Успешно! Попытка номер: {counter}")
                    return ret
                print(f"Не успешно! Попытка номер: {counter}")
            print ("Попыток больше нет")
            return ret
        return wrapper
    return decorator


@retry(times=12)
def flaky_test():
    if time.time() % 2 < 1:
        return "FAILURE"
    return "PASSED"

print(flaky_test())


print ("\n2.	Декоратор проверки прав доступа")
def require_role(role):
    def decorator(func):
        def wrapper(*args):
             if args[0] != role:
                 print(f"Требуется роль {role}, текущая: {args[0]}")
                 return "Failure"
             return func(*args)
        return wrapper
    return decorator


@require_role("admin")
def admin_test(*args):
    print("Выполняется админский тест")
    return "Success"


user_one = "user"
user_two = "admin"
for user in user_one, user_two:
    print(admin_test(user))


print ("\n3.	Декоратор замера времени выполнения")
def timer(func):
    def wrapper(*args):
        start_time = time.time()
        func(*args)
        end_time = time.time()
        print (f"Время выполнения функции {func.__name__} {end_time - start_time}")
    return wrapper


@timer
def slow_test():
    time.sleep(1)
    return "OK"


slow_test()


print("\n4. Декоратор ожидания с таймаутом")
def wait_with_retry_until(**kwargs):
    def decorator(func):
        #@wraps(func)
        def wrapper():
            timeout = kwargs.get("timeout")
            interval = kwargs.get("interval")
            print (f"timeout={timeout}, interval={interval}")
            ret = False
            count = 1
            while ret != True:
                start_time = time.time()
                time.sleep(timeout)
                ret = func()
                end_time = time.time()
                print(f"Попытка {count}: неуспешно" )
                print(f"Время выполнения функции {func.__name__} {end_time - start_time}")
                time.sleep(interval)
                count += 1
            print(f"Попытка {count}: успешно")
            print("Элемент найден")
            print(f"Время выполнения функции {func.__name__} {end_time - start_time}")
        return wrapper
    return decorator


@wait_with_retry_until(timeout=3, interval=0.5)
def element_visible():
    return time.time() % 3 > 2  # имитация появления элемента


element_visible()

print("\n5. Декоратор кэширования результатов.")
def cache_results(func):
    cache_list = {}
    @wraps(func)
    def wrapper(*args, **kwargs):
        if args[0] in cache_list:
            # print ("Найдено в кеше")
            ret = cache_list[args[0]]
        else:
            # print (f"Вычисляем для {args[0]}")
            ret=func(*args, **kwargs)
            cache_list[args[0]] = ret
        return ret
    return wrapper


def count_exec_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        print (f"Выполняю {func.__name__} с аргументом {args[0]}")
        ret=func(*args, **kwargs)
        end = time.time()
        print(ret)
        print(f"Время выполнения: {end - start:.6f} сек")
        return ""
    return wrapper


@count_exec_time
@cache_results
def expensive_calculation(n):
    print(f"Вычисляем для {n}")
    time.sleep(1)
    return n * n


print(expensive_calculation(5)) #медленно считает
print(expensive_calculation(5)) #быстро возвращает из кеша
print(expensive_calculation(5)) #быстро возвращает из кеша
print(expensive_calculation(6)) #медленно считает
print(expensive_calculation(5)) #быстро возвращает из кеша


print("\n6. Декоратор валидации параметров")
def validate_params(decor_param):
    def decorator(func):
        @wraps(func)
        def wrapper(**kwargs):
            for decor_item in decor_param.items():
                #print(f"{kwargs[decor_item[0]]} == {decor_item[1]}")
                if not type(kwargs[decor_item[0]]) == decor_item[1]:
                    print(f"{kwargs[decor_item[0]]} должен быть {decor_item[1].__name__}")
                    return False
            return func(**kwargs)
        return wrapper
    return decorator


@validate_params({"username": str, "age": int})
def create_user(**kwargs):
    return f"Пользователь {kwargs['username']} создан"


print(create_user(username="test", age=25))
print(create_user(username="test", age='25'))


print("\n7. Декоратор условного логирования")
LOG_LEVEL = "DEBUG"
log = lambda string: print(string)

def conditional_log(min_level="INFO"):
    # Извлекаем min_level по-умолчанию (INFO)
    sig = inspect.signature(conditional_log)
    default_val = sig.parameters['min_level'].default
    # print(f"min_level(default)={default_val}")
    # Создаём словарь уровней логирования. Минимальный уровень для показа логов -
    # любой, что выше установленного по-умолчанию
    log_level_range = {"TRACE": 1, "DEBUG": 2, "INFO": 3, "WARN": 4, "ERROR": 5, "FATAL": 6}
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            log_result = func(*args, **kwargs)
            log(log_result) if log_level_range[min_level] > log_level_range[default_val] else False
            return log_result
        return wrapper
    return decorator


@conditional_log("WARN") # лог включен
@conditional_log("INFO") # лог включен
@conditional_log("TRACE") # лог отключен
@conditional_log(LOG_LEVEL) # лог отключен
def debug_test():
    return "debug_result"


debug_test()

