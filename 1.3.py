# Input principal amount, rate, and time
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (in percentage): "))
time = float(input("Enter the time period (in years): "))

# Convert rate from percentage to decimal
rate = rate / 100

# Calculate compound interest
compound_interest = principal * ((1 + rate) ** time - 1)

# Display the compound interest
print("Compound interest:", compound_interest)
