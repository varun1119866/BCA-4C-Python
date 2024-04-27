# Input the value of n
n = int(input("Enter a positive integer: "))

# Initialize the sum
sum_of_natural_numbers = 0

# Compute the sum of the first n natural numbers
for i in range(1, n + 1):
    sum_of_natural_numbers += i

# Display the result
print("Sum of the first", n, "natural numbers:", sum_of_natural_numbers)
