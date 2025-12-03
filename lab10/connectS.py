import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="snake_game",
    user="postgres",
    password="Qwerty1234!"
)

cur = conn.cursor()
