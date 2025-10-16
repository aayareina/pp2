import re

#1
txt = "ab abb a abbb aa"
print(re.findall(r'ab*', txt))

#2
txt = input("Введите текст: ")
print(re.findall(r'ab*', txt))
