import math


# 1
radius = 7
area = math.pi * pow(radius, 2)
print("Площадь круга:", area)

# 2
print("Наибольшее целое, не превышающее 9.8:", math.floor(9.8))

# 3
sin = math.sin(math.radians(45))
print("Синус 45 градусов:", sin)

# 4
print("Корень из 144:", math.sqrt(144))

# 5
print("НОД(270, 192):", math.gcd(270, 192))

# 6
print("e в степени 3:", math.exp(3))

# 7
print("Факториал 8:", math.factorial(8))

# 8
degree = math.log(256, 2)
print("Степень, в которую нужно возвести 2, чтобы получить 256:", degree)

# 9
print("Округление 3.14159 вверх:", math.ceil(3.14159))

# 10
def tangent(angle_deg):
    return math.tan(math.radians(angle_deg))

print("Тангенс 45 градусов:", tangent(45))