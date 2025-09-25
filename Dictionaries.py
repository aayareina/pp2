# Словари
student = {
  "name": "Aigerim",
  "age": 19,
  "major": "Computer Science"
}

print(student["name"])  # → Aigerim

# Изменить значение
student["age"] = 20

# Добавить ключ
student["grade"] = "A"

# Цикл по ключам
for key in student:
    print(key, ":", student[key])

# Только значения
for value in student.values():
    print("Value:", value)
