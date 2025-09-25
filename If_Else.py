temperature = 15

if temperature > 25:
    print("It's hot outside")   # условие ложное
elif temperature >= 15:
    print("The weather is nice")  # сработает это
else:
    print("It's cold")

# Короткая запись
score = 90
if score >= 80: print("Excellent")  # 90 >= 80 → Excellent

# Тернарный оператор
message = "Pass" if score >= 50 else "Fail"
print(message)  # Pass
