# Input sales amount
sales_amount = float(input("Enter the sales amount: "))

# Calculate commission based on the conditions
if sales_amount >= 15000:
    commission = 0.20 * sales_amount
elif sales_amount >= 1000:
    commission = 0.15 * sales_amount
else:
    commission = 0.10 * sales_amount

# Display the calculated commission
print("Commission:", commission)
