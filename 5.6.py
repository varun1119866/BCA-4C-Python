import math

def calculate_mean(numbers):
    return sum(numbers) / len(numbers)

def calculate_variance(numbers):
    mean = calculate_mean(numbers)
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    return variance

def calculate_std_deviation(numbers):
    variance = calculate_variance(numbers)
    std_deviation = math.sqrt(variance)
    return std_deviation

def main():
   
    numbers = [float(x) for x in input("Enter the list of numbers separated by spaces: ").split()]


