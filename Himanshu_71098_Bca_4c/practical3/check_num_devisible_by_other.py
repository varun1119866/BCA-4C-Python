def check_divisibility(num1, num2):
    if num2 == 0:
        return False
    return num1 % num2 == 0

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if check_divisibility(num1, num2):
    print(num1, "is divisible by", num2)
else:
    print(num1, "is not divisible by", num2)
