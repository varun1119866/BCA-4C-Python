def calculate_compound_interest(principal, rate, time):
    return principal * (1 + rate / 100) ** time - principal

principal = float(input("Enter principal amount: "))
rate = float(input("Enter annual interest rate (in percentage): "))
time = float(input("Enter time period (in years): "))

compound_interest = calculate_compound_interest(principal, rate, time)

print("Compound interest:", compound_interest)
