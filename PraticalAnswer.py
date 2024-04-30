#Practical 1 – Simple Introductory Python Programs
#1.1 WAP to Calculate Area and Perimeter of a Rectangle:

def calculate_rectangle_properties(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

area, perimeter = calculate_rectangle_properties(length, width)
print(f"Area of the rectangle: {area}")
print(f"Perimeter of the rectangle: {perimeter}")

#1.2 WAP to calculate Avg. marks of 3 subjects:

def calculate_average_marks(subject1, subject2, subject3):
    average_marks = (subject1 + subject2 + subject3) / 3
    return average_marks

subject1 = float(input("Enter marks for subject 1: "))
subject2 = float(input("Enter marks for subject 2: "))
subject3 = float(input("Enter marks for subject 3: "))

average = calculate_average_marks(subject1, subject2, subject3)
print(f"Average marks: {average}")

#1.3 WAP to compute compound Interest:

def compute_compound_interest(principal, rate, time):
    amount = principal * (1 + rate/100)**time
    compound_interest = amount - principal
    return compound_interest

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (in percentage): "))
time = float(input("Enter the time period (in years): "))

interest = compute_compound_interest(principal, rate, time)
print(f"Compound interest: {interest}")

#Practical 2 – Working with Strings – basic String Operations
#2.1 WAP to demonstrate Slicing Operations in Strings:

# Slicing operations on a string
string = "Hello, World!"

# Print the original string
print("Original String:", string)

# Slicing from index 0 to 5 (exclusive)
print("Slice from index 0 to 5:", string[0:5])

# Slicing from index 7 to the end of the string
print("Slice from index 7 to end:", string[7:])

# Slicing from the beginning to index 5 (exclusive)
print("Slice from beginning to index 5:", string[:5])

# Slicing every second character
print("Every second character:", string[::2])

# Slicing with negative indices
print("Slice using negative indices:", string[-6:-1])

# Reverse the string using slicing
print("Reversed String:", string[::-1])

#2.2 WAP to demonstrate built-in functions of Strings:

# Demonstrating built-in functions of strings
string = "Hello, World!"

# Length of the string
print("Length of the string:", len(string))

# Convert the string to uppercase
print("Uppercase:", string.upper())

# Convert the string to lowercase
print("Lowercase:", string.lower())

# Capitalize the string
print("Capitalized:", string.capitalize())

# Count occurrences of a substring
print("Occurrences of 'l':", string.count('l'))

# Find the index of a substring
print("Index of 'World':", string.find('World'))

# Replace substring
print("Replace 'Hello' with 'Hi':", string.replace('Hello', 'Hi'))

# Split the string into a list based on a delimiter
print("Split by comma:", string.split(','))

# Check if the string starts with a particular substring
print("Starts with 'Hello':", string.startswith('Hello'))

# Check if the string ends with a particular substring
print("Ends with 'World!':", string.endswith('World!'))

#Practical 3 – Conditionals in Python – Decision Control
#3.1 WAP to check if one number is divisible by the other or not:

def check_divisibility(num1, num2):
    if num2 == 0:
        print("Cannot divide by zero!")
    elif num1 % num2 == 0:
        print(f"{num1} is divisible by {num2}")
    else:
        print(f"{num1} is not divisible by {num2}")

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
check_divisibility(num1, num2)
#3.2 WAP to check if a number is positive, negative, or zero:

def check_number(num):
    if num > 0:
        print("Positive number")
    elif num < 0:
        print("Negative number")
    else:
        print("Zero")

num = float(input("Enter a number: "))
check_number(num)
#3.3 WAP to check if a given year is a leap year or not:

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")

year = int(input("Enter a year: "))
is_leap_year(year)

#3.4 WAP to accept basic salary for the employee. Calculate DA and HRA based on salary:

def calculate_salary(bs):
    if bs >= 20000:
        da = 0.3 * bs
        hra = 0.2 * bs
    else:
        da = 0.2 * bs
        hra = 0.1 * bs
    print(f"Basic Salary: {bs}")
    print(f"DA: {da}")
    print(f"HRA: {hra}")

basic_salary = float(input("Enter the basic salary: "))
calculate_salary(basic_salary)

#3.5 WAP to accept sales amount for the salesman. Compute commission based on sales amount:

def calculate_commission(sales_amount):
    if sales_amount >= 15000:
        commission = 0.20 * sales_amount
    elif sales_amount >= 1000:
        commission = 0.15 * sales_amount
    else:
        commission = 0.10 * sales_amount
    print(f"Sales Amount: {sales_amount}")
    print(f"Commission: {commission}")

sales_amount = float(input("Enter the sales amount: "))
calculate_commission(sales_amount)

#Practical 4 – While and For loops – Repetition Control Statements

#4.1 WAP to show working of a while Loop with a text:

# Using while loop with text
text = "Hello, world!"
index = 0
while index < len(text):
    print(text[index], end=" ")
    index += 1
  
#4.2 WAP to show working of a while Loop with Numbers:

# Using while loop with numbers
num = 1
while num <= 10:
    print(num, end=" ")
    num += 1
  
#4.3 WAP to show the working of break and continue statement:

# Using break and continue statements
num = 1
while num <= 10:
    if num == 5:
        num += 1
        continue
    print(num, end=" ")
    if num == 8:
        break
    num += 1
  
#4.4 WAP to the use of else statement with while and break:

# Using else statement with while and break
num = 1
while num <= 5:
    print(num, end=" ")
    if num == 3:
        break
    num += 1
else:
    print("Else block is executed because the loop did not encounter a break statement.")
  
#4.5 WAP to compute the Sum of the Series 4 + 8 + 12 + … + 40:

# Computing the sum of the series
sum_series = 0
num = 4
while num <= 40:
    sum_series += num
    num += 4
print("Sum of the series:", sum_series)

#4.6 Write a program to display the Fibonacci sequences up to nth term where n is provided by the user:

# Displaying Fibonacci sequence up to nth term
n = int(input("Enter the value of n: "))
a, b = 0, 1
count = 0
print("Fibonacci sequence:")
while count < n:
    print(a, end=" ")
    a, b = b, a + b
    count += 1

#4.7 WAP that prints multiplication table of a number using for loop:

# Printing multiplication table of a number using a for loop
num = int(input("Enter a number: "))
print(f"Multiplication table of {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num*i}")
  
#4.8 WAP To print a Triangle Pattern:

# Printing a triangle pattern
rows = 5
for i in range(1, rows + 1):
    print("*" * i)

#4.9 WAP to compute Sum of the series 3 + 6 + 9 + … + 30:

# Computing sum of the series
sum_series = 0
for i in range(3, 31, 3):
    sum_series += i
print("Sum of the series:", sum_series)

#4.10 WAP to print the product of the series m = 15 * 13 * 11 * 9 * 7:

# Computing product of the series
product_series = 15 * 13 * 11 * 9 * 7
print("Product of the series:", product_series)

#4.11 WAP to compute factorial of a Number:

# Computing factorial of a number
num = int(input("Enter a number: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print("Factorial of", num, ":", factorial)

#4.12 WAP to display the Cube of first 10 even numbers:

# Displaying cube of first 10 even numbers
for i in range(2, 21, 2):
    print(f"Cube of {i}:", i ** 3)
  
#4.13 WAP to compute sum of first n natural numbers:

# Computing sum of first n natural numbers
n = int(input("Enter a number: "))
sum_natural = sum(range(1, n + 1))
print("Sum of first", n, "natural numbers:", sum_natural)

#4.14 WAP to display 1 to 10 numbers in reverse order:

# Displaying numbers in reverse order
for i in range(10, 0, -1):
    print(i)
  
#4.15 WAP to create a list of any specific size. Arrange all the elements in ascending order. Display list before and after sorting:

# Creating a list and sorting it
size = int(input("Enter the size of the list: "))
my_list = []
for i in range(size):
    element = int(input(f"Enter element {i+1}: "))
    my_list.append(element)

print("Original list:", my_list)
my_list.sort()
print("Sorted list:", my_list)
# Practical 5 Working with Lists in Python

#5.1 WAP to show the creation and working of lists:

# Creation and working of lists
my_list = [1, 2, 3, 4, 5]
print("Original list:", my_list)

# Adding elements to the list
my_list.append(6)
print("List after appending 6:", my_list)

# Removing elements from the list
my_list.remove(3)
print("List after removing 3:", my_list)

# Accessing elements by index
print("Element at index 2:", my_list[2])

# Slicing the list
print("Sliced list:", my_list[1:4])

#5.2 WAP to print elements of a list ['q','w','e','r','t','y'] in separate lines along with element's both indexes (Positive and Negative):

# Printing elements of a list along with indexes
my_list = ['q', 'w', 'e', 'r', 't', 'y']
for i in range(len(my_list)):
    print(f"Element '{my_list[i]}' has positive index {i} and negative index {-len(my_list)+i}")
  
#5.3 WAP to demonstrate the working of methods used with lists:

# Demonstrating methods used with lists
my_list = [3, 1, 4, 1, 5, 9]

# Append method
my_list.append(2)
print("After appending 2:", my_list)

# Sort method
my_list.sort()
print("After sorting:", my_list)

# Pop method
popped_element = my_list.pop()
print("Popped element:", popped_element)
print("List after popping:", my_list)

# Count method
count_of_1 = my_list.count(1)
print("Count of 1:", count_of_1)

#5.4 WAP to create a 3x3 Matrix and how to extract individual elements of the matrix:

# Creating a 3x3 matrix
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

# Extracting individual elements of the matrix
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(f"Element at row {i}, column {j}: {matrix[i][j]}")
      
#5.5 WAP to demonstrate built-in functions in Lists:

# Demonstrating built-in functions in lists
my_list = [1, 2, 3, 4, 5]

# Length function
print("Length of the list:", len(my_list))

# Maximum function
print("Maximum element of the list:", max(my_list))

# Minimum function
print("Minimum element of the list:", min(my_list))

# Sum function
print("Sum of the elements of the list:", sum(my_list))

#5.6 WAP to calculate the mean, variance, and standard deviation of a given list of numbers:

import statistics

# Given list of numbers
numbers = [10, 20, 30, 40, 50]

# Mean calculation
mean = statistics.mean(numbers)
print("Mean:", mean)

# Variance calculation
variance = statistics.variance(numbers)
print("Variance:", variance)

# Standard deviation calculation
std_deviation = statistics.stdev(numbers)
print("Standard deviation:", std_deviation)
