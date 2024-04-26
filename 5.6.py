# Define the list of numbers
numbers = [10, 20, 30, 40, 50]

# Calculate the mean
mean = sum(numbers) / len(numbers)

# Calculate the variance
variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)

# Calculate the standard deviation
std_deviation = variance ** 0.5

# Display the results
print("List of numbers:", numbers)
print("Mean:", mean)
print("Variance:", variance)
print("Standard Deviation:", std_deviation)
