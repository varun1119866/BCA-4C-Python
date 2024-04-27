def calculate_area(length, width):
    return length * width

def calculate_perimeter(length, width):
    return 2 * (length + width)

def main():
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))

    area = calculate_area(length, width)
    perimeter = calculate_perimeter(length, width)

    print("Area of the rectangle:", area)
    print("Perimeter of the rectangle:", perimeter)

if __name__ == "__main__":
    main()
