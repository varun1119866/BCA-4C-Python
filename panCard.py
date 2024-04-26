import re

def isvalidate(z):
    result = re.compile("[A-Z,a-z]{5}[0-9]{4}[A-Z,a-z]{1}")
    return result.match(z)
print("Name: amarneet \nRoll No: 2210997029\n")
name = input("Enter username: ")
pan_number = input("Enter your PAN number: ")

if isvalidate(pan_number):
    print("Dear,",name,"your PAN number(",pan_number,") is valid.")
else:
    print("Your PAN number is not valid.")
