# 4.1 While loop with text
def while_loop_text():
    count = 0
    while count < 5:
        print("Inside the while loop")
        count += 1

# Test the function
while_loop_text()

# 4.2 While loop with numbers
def while_loop_numbers():
    num = 1
    while num <= 5:
        print(num)
        num += 1

# Test the function
while_loop_numbers()

# 4.3 Working of break and continue statement
def break_continue_demo():
    num = 0
    while num < 10:
        num += 1
        if num == 5:
            continue
        print(num)
        if num == 8:
            break

# Test the function
break_continue_demo()

# 4.4 Use of else statement with while and break
def else_with_while():
    num = 1
    while num <= 5:
        print(num)
        num += 1
    else:
        print("Loop completed successfully")

# Test the function
else_with_while()

# 4.5 Sum of the series 4 + 8 + 12 + ... + 40
def sum_series():
    total = 0
    for i in range(4, 41, 4):
        total += i
    print("Sum of the series:", total)

# Test the function
sum_series()

# 4.6 Fibonacci sequence up to nth term
def fibonacci_sequence(n):
    a, b = 0, 1
    count = 0
    while count < n:
        print(a, end=" ")
        c = a + b
        a = b
        b = c
        count += 1

# Test the function
fibonacci_sequence(10)

# 4.7 Multiplication table using for loop
def multiplication_table(num):
    for i in range(1, 11):
        print(num, "x", i, "=", num * i)

# Test the function
multiplication_table(5)

# 4.8 Printing a Triangle Pattern
def print_triangle(rows):
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "*" * (2 * i - 1))

# Test the function
print_triangle(5)

# 4.9 Sum of the series 3 + 6 + 9 + ... + 30
def sum_series():
    total = 0
    for i in range(3, 31, 3):
        total += i
    print("Sum of the series:", total)

# Test the function
sum_series()

# 4.10 Product of the series m = 15 * 13 * 11 * 9 * 7
def product_series():
    product = 15
    for i in range(13, 6, -2):
        product *= i
    print("Product of the series:", product)

# Test the function
product_series()

# 4.11 Factorial of a Number
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print("Factorial of", n, "is:", fact)

# Test the function
factorial(5)

# 4.12 Cube of first 10 even numbers
def cube_even_numbers():
    for i in range(2, 21, 2):
        print("Cube of", i, "is:", i ** 3)

# Test the function
cube_even_numbers()

# 4.13 Sum of first n natural numbers
def sum_of_natural_numbers(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    print("Sum of first", n, "natural numbers:", total)

# Test the function
sum_of_natural_numbers(5)

# 4.14 Display 1 to 10 numbers in reverse order
def reverse_numbers():
    for i in range(10, 0, -1):
        print(i)

# Test the function
reverse_numbers()

# 4.15 Create a list of specific size. Arrange elements in ascending order.
def sort_list(size, elements):
    print("List before sorting:", elements)
    elements.sort()
    print("List after sorting:", elements)

# Test the function
size = 5
elements = [5, 2, 7, 1, 3]
sort_list(size, elements)
