def calculate_compound_interest(principal, rate, time, n):
    
    amount = principal * (1 + rate / n) ** (n * time)
    compound_interest = amount - principal
    return compound_interest

def main():
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the annual interest rate (in percentage): "))
    time = float(input("Enter the time period (in years): "))
    n = int(input("Enter the number of times interest is compounded per year: "))

    rate = rate / 100  

    compound_interest = calculate_compound_interest(principal, rate, time, n)

    print("Compound Interest:", compound_interest)

if __name__ == "__main__":
    main()
