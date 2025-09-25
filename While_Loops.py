count = 1
while count <= 3:
    print("Iteration", count)  # Iteration 1, Iteration 2, Iteration 3
    count += 1

# Break
num = 1
while num < 10:
    if num == 4:
        break  # остановим цикл
    print(num)  # 1, 2, 3
    num += 1

# Continue
i = 0
while i < 6:
    i += 1
    if i % 2 == 0:
        continue  # пропустим четные
    print("Odd:", i)  # 1, 3, 5
