import os
path = "."  

print("Папки:")
for i in os.listdir(path):
    if os.path.isdir(i):
        print(i)

print("Файлы:")
for i in os.listdir(path):
    if os.path.isfile(i):
        print(i)

print (os.listdir(path))
