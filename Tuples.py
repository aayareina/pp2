# Кортежи
animals = ("cat", "dog", "parrot")
print(animals[0])  # индекс 0 → cat

# Распаковка
(x, y, z) = animals
print(x, y, z)  # cat dog parrot

# Кортеж с одним элементом
single = ("apple",)
print(type(single))  # → <class 'tuple'>

# Цикл
for pet in animals:
    print("Pet:", pet)  # выводим каждый элемент кортежа
