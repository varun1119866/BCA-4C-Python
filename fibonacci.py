n = int(input("Enter the number of terms: "))

a, b = 0, 1
count = 0

while count < n:
    print(a, end=" ")
    a, b = b, a + b
    count += 1
    
    # Check if the number of terms required has been printed
    if count == n:
        break
