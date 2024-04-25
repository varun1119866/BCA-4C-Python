Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# 3.1 Check if one number is divisible by the other
def check_divisibility(num1, num2):
    if num1 % num2 == 0:
        print(num1, "is divisible by", num2)
    else:
        print(num1, "is not divisible by", num2)

# Test the function
check_divisibility(10, 5)
check_divisibility(10, 3)

# 3.2 Check if a number is positive, negative, or zero
def check_number(num):
    if num > 0:
        print(num, "is positive")
    elif num < 0:
        print(num, "is negative")
    else:
        print(num, "is zero")

# Test the function
check_number(10)
check_number(-5)
check_number(0)

# 3.3 Check if a given year is leap or not
def check_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
...         print(year, "is a leap year")
...     else:
...         print(year, "is not a leap year")
... 
... # Test the function
... check_leap_year(2020)
... check_leap_year(2021)
... 
... # 3.4 Calculate DA and HRA for an employee's basic salary
... def calculate_salary(bs):
...     if bs >= 20000:
...         DA = 0.3 * bs
...         HRA = 0.2 * bs
...     else:
...         DA = 0.2 * bs
...         HRA = 0.1 * bs
...     print("Basic Salary:", bs)
...     print("DA:", DA)
...     print("HRA:", HRA)
... 
... # Test the function
... calculate_salary(25000)
... calculate_salary(15000)
... 
... # 3.5 Compute commission for a salesman based on sales amount
... def calculate_commission(sales_amount):
...     if sales_amount >= 15000:
...         commission = 0.2 * sales_amount
...     elif sales_amount >= 1000:
...         commission = 0.15 * sales_amount
...     else:
...         commission = 0.1 * sales_amount
...     print("Sales Amount:", sales_amount)
...     print("Commission:", commission)
... 
... # Test the function
... calculate_commission(20000)
... calculate_commission(5000)
... calculate_commission(500)
