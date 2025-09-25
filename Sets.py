# Множества
colors = {"red", "green", "blue"}
print(colors)  # порядок может быть разным

# Добавить
colors.add("yellow")
print(colors)  # {'red', 'green', 'blue', 'yellow'}

# Добавить несколько
colors.update(["black", "white"])
print(colors)  # {'blue', 'yellow', 'green', 'black', 'red', 'white'}

# Удалить
colors.discard("green")
print(colors)  # green удален

# Цикл
for color in colors:
    print("Color:", color)
