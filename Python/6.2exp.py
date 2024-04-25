print("Name: Anshu\n Rollno.: 2210997037")
def abc(l,d,v1,v2):
    l[2]=8
    d['b']=9
    v1=9
    v2=10
    return l,d,v1,v2
List=[1,2,3]
dict={'a':2,'b':3,'c':4}
var1=3
var2=4
n1,n2,n3,n4=abc(List,dict,var1,var2)
print("After changes the method,the updated values are:")
print("List=",n1)
print("Dictionary:",n2)
print("1st Variable:",n3)
print("2nd Variable:",n4)
