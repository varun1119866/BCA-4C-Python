# Input the number
number = int(input("Enter a number: "))

# Initialize the factorial to 1
factorial = 1

# Compute the factorial
for i in range(1, number + 1):
    factorial *= i

# Display the result
print("Factorial of", number, "is:", factorial)
