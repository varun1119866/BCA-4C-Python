def calculate_rectangle_area(length, width):
    return length * width

def calculate_rectangle_perimeter(length, width):
    return 2 * (length + width)

length = float(input("Enter length of rectangle: "))
width = float(input("Enter width of rectangle: "))

area = calculate_rectangle_area(length, width)
perimeter = calculate_rectangle_perimeter(length, width)

print("Area of rectangle:", area)
print("Perimeter of rectangle:", perimeter)
