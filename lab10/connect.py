import psycopg2

conn = psycopg2.connect(
    host="localhost",
    dbname="phonebook",
    user="postgres",
    password="Qwerty1234!"   
)

cur = conn.cursor()

print("Connected successfully!")
