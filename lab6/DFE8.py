f = "delete_me.txt"
import os
if os.path.exists(f) and os.access(f, os.W_OK):
    os.remove(f)
    print(f, "удален")
else:
    print("Файл не существует или нельзя удалить")
