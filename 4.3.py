# Demonstrate the break statement
print("Demonstrating the break statement:")
for i in range(1, 6):
    if i == 4:
        break
    print("Current number:", i)
print("Loop ended.")

# Demonstrate the continue statement
print("\nDemonstrating the continue statement:")
for j in range(1, 6):
    if j == 3:
        continue
    print("Current number:", j)
print("Loop ended.")
