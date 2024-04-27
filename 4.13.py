def sum_of_natural_numbers(n):
    return n * (n + 1) // 2

def main():
    n = int(input("Enter the value of n: "))
    if n < 1:
        print("Please enter a positive integer.")
    else:
        sum_n = sum_of_natural_numbers(n)
        print("Sum of the first", n, "natural numbers is:", sum_n)

if __name__ == "__main__":
    main()
