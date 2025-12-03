from connect import conn, cur

print("1 - поиск по шаблону")
print("2 - вставить или обновить пользователя")
print("3 - массовая вставка пользователей")
print("4 - пагинация")
print("5 - удалить пользователя")
choice = input("Выберите действие: ")

# 1) поиск по шаблону
if choice == "1":
    pattern = input("Введите шаблон: ")
    cur.execute("SELECT * FROM search_by_pattern(%s)", (pattern,))
    rows = cur.fetchall()
    for r in rows:
        print(r)

# 2) вставка или обновление
elif choice == "2":
    name = input("Имя: ")
    phone = input("Телефон: ")
    cur.execute("CALL insert_or_update_user(%s, %s)", (name, phone))
    conn.commit()
    print("Готово. Смотри pgAdmin.")

# 3) массовая вставка
elif choice == "3":
    kol = int(input("Сколько добавить?: "))
    names = []
    phones = []

    for i in range(kol):
        names.append(input("Имя: "))
        phones.append(input("Телефон: "))

    cur.execute("CALL insert_many_users(%s, %s)", (names, phones))
    conn.commit()
    print("Готово.")

# 4) пагинация
elif choice == "4":
    limit = int(input("limit: "))
    offset = int(input("offset: "))
    cur.execute("SELECT * FROM get_paginated(%s, %s)", (limit, offset))
    rows = cur.fetchall()
    for r in rows:
        print(r)

# 5) удалить
elif choice == "5":
    val = input("Имя или телефон: ")
    cur.execute("CALL delete_user(%s)", (val,))
    conn.commit()
    print("Удалено.")

cur.close()
conn.close()
