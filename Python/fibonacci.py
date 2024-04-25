# fibonacci.py
def fab(num):
    a=0
    b=1
    if num==1:
        print(a, end=" ")
    else:
        print(a, end=" ")
        print(b, end=" ")
        for i in range(2,num):
            c=a+b
            a=b
            b=c
            print(c, end=" ")
print("Anshu 2210997037")
