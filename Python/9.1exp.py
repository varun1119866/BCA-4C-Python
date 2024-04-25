mydict = {}

for i in range(5):
    print("====================================================================")
    roll_no = int(input("Enter your Roll no: "))
    name = input("Enter your Name: ")
    age = int(input("Enter your Age: "))
    stream = input("Enter your Stream: ")
    contactNo = input("Enter your Contact no: ")
    mydict[roll_no] = {name, age, stream, contactNo}
    print("====================================================================")

search = int(input("Enter the Roll Number you want to search: "))
if search in mydict.keys():
    print("Details of Roll Number", search, ":")
    for val in mydict[search]:
        print(val)
else:
    print(str(search) + " was not found")
print("Anshu 2210997037")
