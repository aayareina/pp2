f1 = open("source.txt", "r")
f2 = open("destination.txt", "w")
for line in f1:
    f2.write(line)
f1.close()
f2.close()
