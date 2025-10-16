#1
txt = "hello_world_example"
print(''.join(w.title() for w in txt.split('_')))

#2
txt = input("Введите строку в snake_case: ")
print(''.join(w.title() for w in txt.split('_')))
