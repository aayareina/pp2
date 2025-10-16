import re

#1
txt = "ab abb abbb abbbb"
print(re.findall(r'ab{2,3}', txt))

#2
txt = input("Введите текст: ")
print(re.findall(r'ab{2,3}', txt))
