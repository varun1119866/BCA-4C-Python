def multiplication_table(number):
    print("Multiplication Table of", number)
    for i in range(1, 11):
        print(number, "x", i, "=", number * i)

def main():
    number = int(input("Enter the number to print its multiplication table: "))
    multiplication_table(number)

if __name__ == "__main__":
    main()
