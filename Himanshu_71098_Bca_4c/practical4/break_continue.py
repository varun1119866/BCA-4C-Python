# Example of break statement
num = 1

while num <= 10:
    if num == 5:
        break
    print(num)
    num += 1

# Example of continue statement
num = 1

while num <= 10:
    if num == 5:
        num += 1
        continue
    print(num)
    num += 1
