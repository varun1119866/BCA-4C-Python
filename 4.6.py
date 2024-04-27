# Input the number of terms from the user
n = int(input("Enter the number of terms for Fibonacci sequence: "))

# Initialize variables for the first two terms
first_term = 0
second_term = 1

# Display the Fibonacci sequence
print("Fibonacci sequence up to", n, "terms:")
print(first_term)  # Print the first term
print(second_term)  # Print the second term

# Compute and print the remaining terms
for _ in range(2, n):
    next_term = first_term + second_term
    print(next_term)
    # Update variables for the next iteration
    first_term = second_term
    second_term = next_term
