# 1. Градусы в радианы
import math

deg = float(input("Введите градусы: "))
rad = math.radians(deg)
print("В радианах:", rad)

# 2. Площадь трапеции
h = float(input("Высота: "))
a = float(input("Основание 1: "))
b = float(input("Основание 2: "))
area = (a + b) / 2 * h
print("Площадь:", area)

# 3. Площадь многоугольника
import math

n = int(input("Количество сторон: "))
side = float(input("Длина стороны: "))
area = (n * side ** 2) / (4 * math.tan(math.pi / n))
print("Площадь многоугольника:", area)

# 4. Площадь параллелограмма
base = float(input("Основание: "))
height = float(input("Высота: "))
area = base * height
print("Площадь:", area)
