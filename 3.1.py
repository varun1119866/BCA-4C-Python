def check_divisibility(number, divisor):
    if number % divisor == 0:
        return True
    else:
        return False

def main():
    number = float(input("Enter the number: "))
    divisor = float(input("Enter the divisor: "))

    if check_divisibility(number, divisor):
        print("{} is divisible by {}".format(number, divisor))
    else:
        print("{} is not divisible by {}".format(number, divisor))

if __name__ == "__main__":
    main()
