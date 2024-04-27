import math

def calculate_mean(numbers):
    return sum(numbers) / len(numbers)

def calculate_variance(numbers):
    mean = calculate_mean(numbers)
    return sum((x - mean) ** 2 for x in numbers) / len(numbers)

def calculate_standard_deviation(numbers):
    variance = calculate_variance(numbers)
    return math.sqrt(variance)

# Example list of numbers
numbers = [5, 10, 15, 20, 25]

mean = calculate_mean(numbers)
variance = calculate_variance(numbers)
standard_deviation = calculate_standard_deviation(numbers)

print("Mean:", mean)
print("Variance:", variance)
print("Standard Deviation:", standard_deviation)
