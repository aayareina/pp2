cities = ["Almaty", "Astana", "Shymkent"]

# Простой цикл
for city in cities:
    print("City:", city)  # выводим каждый город

# По строке
for ch in "KBTU":
    print(ch)  # K B T U

# Break
for city in cities:
    if city == "Astana":
        break
    print(city)  # Almaty

# Continue
for city in cities:
    if city == "Astana":
        continue
    print(city)  # Almaty, Shymkent

# Range
for num in range(2, 8):
    print("Number:", num)  # 2 3 4 5 6 7

# Вложенные циклы
drinks = ["tea", "coffee"]
for c in cities:
    for d in drinks:
        print(c, "-", d)  # каждая комбинация города и напитка
