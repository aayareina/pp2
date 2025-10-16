import re

#1
txt = "Hello, world. How are you"
print(re.sub(r'[ ,.]+', ':', txt))

#2
txt = input("Введите текст: ")
print(re.sub(r'[ ,.]+', ':', txt))
