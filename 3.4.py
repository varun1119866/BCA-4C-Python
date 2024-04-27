# Input basic salary
basic_salary = float(input("Enter the basic salary: "))

# Calculate DA and HRA based on the conditions
if basic_salary >= 20000:
    da = 0.3 * basic_salary
    hra = 0.2 * basic_salary
else:
    da = 0.2 * basic_salary
    hra = 0.1 * basic_salary

# Display the calculated DA and HRA
print("Dearness Allowance (DA):", da)
print("House Rent Allowance (HRA):", hra)
