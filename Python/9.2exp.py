mydict = {}

for i in range(2):
    print("====================================================================")
    phone_no = input("Enter your Phone no: ")
    name = input("Enter your Name: ")
    if len(phone_no)!=10 or phone_no=="":
        print("Please Enter the Correct Phone Number")
        continue
    mydict[phone_no] = name
    print("====================================================================")

find = input("Enter the Roll Number you want to search: ")
if find in mydict.keys():
    print(find +"->"+mydict[find])
else:
    print("Number not found!!")
print("Anshu 2210997037")
