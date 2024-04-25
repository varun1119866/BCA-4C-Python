print("Name: Anshu\n Rollno.: 2210997037")
s1=["Yuvraj","Raj","Tanvi","Tanmay","Abhishek","Tanmay","Tarun","Shourya","Sarthak","Shiva","Aman","Raj","Shruti","Gaurav","Akash"]
startValue=int(input("Enter the Start index:"))
endValue=int(input("Enter the End index:"))
sliced_em=s1[startValue:endValue]
for i in sliced_em:
    print(i,len(i))
