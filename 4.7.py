# Input the number for which multiplication table is to be printed
number = int(input("Enter a number: "))

# Display the multiplication table using a for loop
print("Multiplication table of", number, ":")
for i in range(1, 11):
    print(number, "x", i, "=", number * i)
