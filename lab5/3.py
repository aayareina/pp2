import re

#1
txt = "hello_world test_python hi_Bye"
print(re.findall(r'[a-z]+_[a-z]+', txt))

#2
txt = input("Введите текст: ")
print(re.findall(r'[a-z]+_[a-z]+', txt))
