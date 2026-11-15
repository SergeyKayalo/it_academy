import pytest
from pytest_check import check
import practice_calculator as calc


mycalc = calc.Calculator()
count = 0

# ------------------------------- История вычислений ---------------
# у нового калькулятора история пустая.
def test_history_empty_by_default():
    assert mycalc.get_history() == []

# после сложения в истории появляется запись.
def test_history_after_add():
    mycalc.add(1, 2)
    assert len(mycalc.get_history()) == 1

# после clear_history() история становится пустой.
def test_clear_history():
    mycalc.clear_history()
    assert mycalc.get_history() == []

# после нескольких операций история содержит все записи.
def test_history_after_multiple_operations ():
    for x in range(3):
        mycalc.add(x, 2)
    assert len(mycalc.get_history()) == 3

# записи в истории идут в порядке выполнения операций.
def test_history_order():
    exp = []
    for x in range(3):
        exp.append(f"{x} + {2} = {x + 2}")
    assert mycalc.get_history() == exp

# изменение списка, полученного из get_history(), не меняет историю калькулятора.
def test_get_history_returns_copy():
    after = mycalc.get_history()
    mycalc.get_history().append("3 + 3 = 6")
    assert mycalc.get_history() == after

# при делении на ноль запись в историю не добавляется.
def test_history_not_added_after_error ():
    after = mycalc.get_history()
    try:
        mycalc.divide(10,0)
    except ZeroDivisionError:
        pass
    finally: assert mycalc.get_history() == after


# ------------------------ сложение ----------------------------------
# сложение двух положительных чисел.
@pytest.mark.parametrize("a, b, exp",
[
    (1, 2, 3),
    (4, 5, 9)
])
def test_add_positive_numbers(a,b, exp):
    with check:
        assert mycalc.add(a, b) == exp

# сложение числа с нулём.
@pytest.mark.parametrize("a, b, exp",
[
    (1, 0, 1),
    (4, 0, 4)
])
def test_add_with_zero(a,b, exp):
    with check:
        assert mycalc.add(a, b) == exp

# сложение отрицательных чисел.
@pytest.mark.parametrize("a, b, exp",
[
    (-1, 1, 0),
    (-4, -3, -7)
])
def test_add_negative_numbers(a,b, exp):
    with check:
        assert mycalc.add(a, b) == exp

# сложение чисел с плавающей точкой.
@pytest.mark.parametrize("a, b, exp",
[
    (1.1, 1.5, 2.6),
    (-4.1, -3, -7.1)
])
def test_add_float_numbers(a,b, exp):
    with check:
        assert mycalc.add(a, b) ==  pytest.approx(exp)

# --------------------- вычитание -------------------------------------
# вычитание положительных чисел. Универсальный вариант (все тесты в одном)
@pytest.mark.parametrize("a, b, exp",
[
    (10, 2, 8),
    (101, 1, 100),
    (10, 20, -10),
    (-10, - 2, -8),
    (0.3, 0.1, 0.2),
    (12.9, 2.9, 10.0)
])
def test_subtract_positive_numbers(a,b, exp):
    with check:
         if not a.is_integer() or not b.is_integer():
             exp = pytest.approx(exp)
         assert mycalc.subtract(a, b) == exp

# ----------------------------------- умножение -----------------------
# умножение положительных чисел
@pytest.mark.parametrize("a, b, exp",
[
    (10, 2, 20),
    (2, 3, 6)
])
def test_multiply_positive_numbers(a,b, exp):
    with check:
        assert mycalc.multiply(a, b) == exp

# умножение на ноль.
@pytest.mark.parametrize("a, b, exp",
[
    (10, 0, 0),
    (101, 0, 0)
])
def test_multiply_by_zero(a,b, exp):
    with check:
        assert mycalc.multiply(a, b) == exp

# умножение отрицательных чисел.
@pytest.mark.parametrize("a, b, exp",
[
    (10, -1, -10),
    (-101, -2, 202)
])
def test_multiply_negative_numbers(a,b, exp):
    with check:
        assert mycalc.multiply(a, b) == exp

# умножение дробных чисел.
@pytest.mark.parametrize("a, b, exp",
[
    (10.1, -1.1, -11.11),
    (101, 2.1, 212.1)
])
def test_multiply_float_numbers(a,b, exp):
    with check:
        assert mycalc.multiply(a, b) == pytest.approx(exp)

# ----------------------------- деление ---------------------------------
# деление положительных чисел
@pytest.mark.parametrize("a, b, exp",
[
    (10, 2, 5),
    (100, 5, 20)
])
def test_divide_positive_numbers(a,b, exp):
    with check:
        assert mycalc.divide(a, b) == exp

# деление отрицательных чисел.
@pytest.mark.parametrize("a, b, exp",
[
    (-10, -2, 5),
    (-100, 5, -20)
])
def test_divide_negative_numbers(a,b, exp):
    with check:
        assert mycalc.divide(a, b) == exp

# результат деления всегда float.
@pytest.mark.parametrize("a, b, exp",
[
    (-11.66, -2.2, 5.3),
    (-103.02, 5.1, -20.2)
])
def test_divide_result_is_float (a,b, exp):
    with check:
        assert mycalc.divide(a, b) == pytest.approx(exp)

#------------------------------- Возведение в степень -----------------------------
# возведение в положительную степень.
@pytest.mark.parametrize("a, b, exp",
[
    (2, 3, 8),
    (4, 2, 16)
])
def test_power_positive_exponent(a,b, exp):
    with check:
        assert mycalc.power(a, b) == exp

# возведение в нулевую степень.
@pytest.mark.parametrize("a, b, exp",
[
    (2, 0, 1),
    (4, 0, 1)
])
def test_power_zero_exponent (a,b, exp):
    with check:
        assert mycalc.power(a, b) == exp

# возведение в отрицательную степень.
@pytest.mark.parametrize("a, b, exp",
[
    (2, -3, 0.125),
    (-2, -3, -0.125)
])
def test_power_negative_exponent (a,b, exp):
    with check:
        assert mycalc.power(a, b) == pytest.approx(exp)

# ---------------------------- Процент от числа ------------------------------
# расчёт процента от положительного числа.
@pytest.mark.parametrize("a, b, exp",
[
    (80, 50, 40),
    (40, 20, 8)
])
def test_percentage_positive_value (a,b, exp):
    with check:
        assert mycalc.percentage(a, b) == pytest.approx(exp)

# 0% от числа равен 0.
def test_percentage_zero_percent ():
    with check:
        assert mycalc.percentage(0, 0) == 0

# 100% от числа равно самому числу.
@pytest.mark.parametrize("a, b",
[
    (100, 50),
    (100, 20)
])
def test_percentage_hundred_percent  (a,b):
    with check:
        assert mycalc.percentage(a, b) == b


# ------------------------------------- Проверка ошибок -------------------------
# текст исключения содержит "Деление на ноль".
def test_divide_by_zero_error_message():
    with pytest.raises(ZeroDivisionError) as err_info:
        mycalc.divide(10, 0)
    assert "Деление на ноль" in str(err_info.value)

# передача отрицательного числа в percentage() вызывает ValueError,
# текст исключения содержит "Процент не может быть отрицательным".
def test_percentage_negative_error_message():
    with pytest.raises(ValueError) as err_info:
        mycalc.percentage(100, -10)
    assert "Процент не может быть отрицательным" in str(err_info.value)

# передача строки в add() вызывает TypeError
def test_invalid_types_add():
    with pytest.raises(TypeError):
        assert mycalc.add(100, "-10")

# передача строки в divide() вызывает TypeError.
def test_invalid_types_divide():
    with pytest.raises(TypeError):
        assert mycalc.divide(100, "-10")
























# @pytest.mark.parametrize("a, b, exception",
# [
#     (10, 0, pytest.raises(ZeroDivisionError)),
#     (101, 0, pytest.raises(ZeroDivisionError)),
# ])
# def test_multiply_by_zero(a,b, exception):
#     with exception:
#         with check:
#             assert mycalc.multiply(a, b) == 0





