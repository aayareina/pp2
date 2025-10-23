text = "You belong to ME"  
big = 0
small = 0
for c in text:
    if c.isupper():
        big += 1
    elif c.islower():
        small += 1
print("Upper:", big)
print("Lower", small)
