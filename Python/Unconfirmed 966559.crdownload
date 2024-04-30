def compound_interest(principal, rate, time):
    
    amount = principal * (pow((1 + rate / 100), time))
    interest = amount - principal
    return interest

def main():
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the annual interest rate (in percentage): "))
    time = float(input("Enter the time period (in years): "))

    interest = compound_interest(principal, rate, time)

    print("Compound interest:", interest)

if __name__ == "__main__":
    main()
