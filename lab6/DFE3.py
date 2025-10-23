import os
p = "example.txt"
if os.path.exists(p):
    print("Существует")
    print("Имя файла:", os.path.basename(p))
    print("Папка:", os.path.dirname(p))
else:
    print("Не существует")
