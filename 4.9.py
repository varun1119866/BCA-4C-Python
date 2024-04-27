# Initialize variables
sum_of_series = 0
start = 3
end = 30
step = 3

# Compute the sum of the series
current_number = start
while current_number <= end:
    sum_of_series += current_number
    current_number += step

# Display the result
print("Sum of the series:", sum_of_series)
