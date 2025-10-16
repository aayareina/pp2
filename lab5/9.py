import re

#1
txt = "HelloWorldPython"
print(re.sub(r'([A-Z])', r' \1', txt).strip())

#2
txt = input("Введите CamelCase строку: ")
print(re.sub(r'([A-Z])', r' \1', txt).strip())
