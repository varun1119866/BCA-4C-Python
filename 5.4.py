def create_matrix():
    matrix = []
    for i in range(3):
        row = []
        for j in range(3):
            element = int(input("Enter element at position ({},{}) of the matrix: ".format(i+1, j+1)))
            row.append(element)
        matrix.append(row)
    return matrix

def extract_elements(matrix):
    print("\nMatrix:")
    for row in matrix:
        print(row)

    print("\nIndividual Elements:")
    for i in range(3):
        for j in range(3):
            print("Element at position ({},{}) is: {}".format(i+1, j+1, matrix[i][j]))

def main():
    print("Enter elements for a 3x3 matrix:")
    matrix = create_matrix()
    extract_elements(matrix)

if __name__ == "__main__":
    main()
