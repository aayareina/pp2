# 1. Генератор квадратов чисел
def squares(n):
    for i in range(n + 1):
        yield i * i   # возвращаем квадрат каждого числа

for x in squares(5):
    print(x)


# 2. Генератор четных чисел
def even_numbers(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

n = int(input("Введите число: "))
print(",".join(str(x) for x in even_numbers(n)))

# 3. Числа делящиеся на 3 и 4
def div_3_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

for x in div_3_4(50):
    print(x)

# 4. Квадраты чисел от a до b
def square_range(a, b):
    for i in range(a, b + 1):
        yield i * i

for x in square_range(2, 6):
    print(x)

# 5. От n до 0
def countdown(n):
    for i in range(n, -1, -1):
        yield i

for num in countdown(5):
    print(num)
