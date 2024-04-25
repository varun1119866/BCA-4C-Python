print("Name: Anshu\n Rollno.: 2210997037")
def argument(*args, **kwargs):
    print("Positional Arguments: ")
    for arg in args:
        print(arg)
    print("Keywords Arguments: ")
    for key, value in kwargs.items():
        print(f"{key}:{value}")
        
argument(1,2,3, name= "Dhruv", age= 19)
