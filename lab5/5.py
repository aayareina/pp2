import re

#1
txt = "acb a123b a_b axxxb ab"
print(re.findall(r'a.*b', txt))

#2
txt = input("Введите текст: ")
print(re.findall(r'a.*b', txt))
