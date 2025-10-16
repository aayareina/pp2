import re

#1
txt = "Hello hi World Yes ok Test"
print(re.findall(r'[A-Z][a-z]+', txt))

#2
txt = input("Введите текст: ")
print(re.findall(r'[A-Z][a-z]+', txt))
