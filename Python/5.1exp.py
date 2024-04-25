def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
    
print("Name: Anshu\n Rollno.: 2210997037")
n= int(input("Enter the number: "))
print(f"Factorial of {n} is {fact(n)}")
