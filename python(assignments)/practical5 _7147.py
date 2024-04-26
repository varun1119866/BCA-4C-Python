# 5.1 Creation and working of lists
def working_with_lists():
    my_list = [1, 2, 3, 4, 5]
    print("Original list:", my_list)
    
    # Appending an element
    my_list.append(6)
    print("List after appending:", my_list)
    
    # Removing an element
    my_list.remove(3)
    print("List after removing:", my_list)
    
    # Accessing elements
    print("First element:", my_list[0])
    print("Last element:", my_list[-1])

# Test the function
working_with_lists()

# 5.2 Printing elements of a list in separate lines with their indexes
def print_elements_with_indexes():
    my_list = ['q', 'w', 'e', 'r', 't', 'y']
    for i in range(len(my_list)):
        print("Element:", my_list[i], "Positive index:", i, "Negative index:", i - len(my_list))

# Test the function
print_elements_with_indexes()

# 5.3 Working of methods used with lists
def list_methods_demo():
    my_list = [1, 2, 3, 4, 5]
    print("Original list:", my_list)
    
    # Adding elements
    my_list.append(6)
    my_list.extend([7, 8])
    print("List after adding elements:", my_list)
    
    # Removing elements
    my_list.remove(3)
    my_list.pop()
    print("List after removing elements:", my_list)
    
    # Reversing
    my_list.reverse()
    print("List after reversing:", my_list)

# Test the function
list_methods_demo()

# 5.4 Creating a 3x3 matrix and extracting individual elements
def matrix_operations():
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    print("Original matrix:")
    for row in matrix:
        print(row)
    
    # Extracting individual elements
    print("Element at row 2, column 3:", matrix[1][2])
    print("Element at row 3, column 1:", matrix[2][0])

# Test the function
matrix_operations()

# 5.5 Demonstrating built-in functions in lists
def list_functions_demo():
    my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    print("Original list:", my_list)
    
    # Length of the list
    print("Length of the list:", len(my_list))
    
    # Maximum and minimum
    print("Maximum element:", max(my_list))
    print("Minimum element:", min(my_list))
    
    # Sorting
    my_list.sort()
    print("Sorted list:", my_list)
    
    # Counting occurrences
    print("Count of 5:", my_list.count(5))

# Test the function
list_functions_demo()

# 5.6 Calculating mean, variance, and standard deviation of a list
import statistics

def calculate_statistics(numbers):
    print("List of numbers:", numbers)
    mean = statistics.mean(numbers)
    variance = statistics.variance(numbers)
    std_deviation = statistics.stdev(numbers)
    
    print("Mean:", mean)
    print("Variance:", variance)
    print("Standard Deviation:", std_deviation)

# Test the function
numbers = [1, 2, 3, 4, 5]
calculate_statistics(numbers)
