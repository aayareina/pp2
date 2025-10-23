f = open("example.txt", "r")
lines = f.readlines()
f.close()
print("Количество строк:", len(lines))
