# Create a 3x3 matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Display the matrix
print("Matrix:")
for row in matrix:
    print(row)

# Extract individual elements of the matrix
print("\nIndividual Elements:")
for i in range(3):
    for j in range(3):
        print("Element at row", i, "and column", j, ":", matrix[i][j])
