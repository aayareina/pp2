# Списки
cars = ["BMW", "Tesla", "Toyota"]
print(cars[2])   # элемент с индексом 2 → Toyota

# Изменить элемент
cars[0] = "Audi"
print(cars)  # ['Audi', 'Tesla', 'Toyota']

# Добавить
cars.append("Honda")
print(cars)  # ['Audi', 'Tesla', 'Toyota', 'Honda']

# Вставить на позицию
cars.insert(1, "Mercedes")
print(cars)  # ['Audi', 'Mercedes', 'Tesla', 'Toyota', 'Honda']

# Удалить элемент по индексу
cars.pop(2)
print(cars)  # ['Audi', 'Mercedes', 'Toyota', 'Honda']

# Цикл
for car in cars:
    print("Car:", car)  # выводим каждый элемент списка
