import re

#1
txt = "HelloWorldPython"
print(re.findall(r'[A-Z][a-z]*', txt))

#2
txt = input("Введите CamelCase строку: ")
print(re.findall(r'[A-Z][a-z]*', txt))
