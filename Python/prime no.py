#prime.py
def prime_function(num):
    prime = 1
    for i in range(2,num):
        if(num%i==0):
            prime = 0
            break
    if(prime==0):
        print(f"{num} is not a prime number.")
    else:
        print(f"{num} is a prime number.")
print("Anshu 2210997037")
