# Creating a 3x3 matrix
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

# Extracting individual elements
for i in range(3):
    for j in range(3):
        print("Element at row", i, "column", j, ":", matrix[i][j])
