from connectS import conn, cur

print("1 - добавить")
print("2 - показать")
print("3 - удалить")

choice = input("Выберите: ")

if choice == "1":
    name = input("Имя: ")
    phone = input("Телефон: ")
    cur.execute("INSERT INTO phonebook(name, phone) VALUES(%s, %s)", (name, phone))
    conn.commit()
    print("Добавлено")

elif choice == "2":
    cur.execute("SELECT * FROM phonebook")
    rows = cur.fetchall()
    for r in rows:
        print(r)

elif choice == "3":
    name = input("Кого удалить: ")
    cur.execute("DELETE FROM phonebook WHERE name=%s", (name,))
    conn.commit()
    print("Удалено")

cur.close()
conn.close()
