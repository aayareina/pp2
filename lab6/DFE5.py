lst = ["konjimin", "chocopie", "insulin"]
f = open("bts.txt", "w")
for i in lst:
    f.write(i + "\n")
f.close()
