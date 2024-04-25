print("Name: Anshu\n Rollno.: 2210997037")
print("Income tax calculator:")
bs_sal = float(input("Please enter your salary in rupees: "))
tax = 0
rt = 0
if (bs_sal > 1500000):
    rt = 30
    tax = 0.3 * bs_sal
elif (1200001 <= bs_sal < 1500000):
    rt = 20
    tax = 0.2 * bs_sal
elif (900001 <= bs_sal < 1200000):
    rt = 15
    tax = 0.15 * bs_sal
elif (600001 <= bs_sal < 900000):
    rt = 10
    tax = 0.1 * bs_sal
elif (300001 <= bs_sal < 600000):
    rt = 5
    tax = 0.05 * bs_sal
gr_sal = bs_sal - tax
print("\nYour basic salary = Rs.", bs_sal, sep="")
print("Income tax rate = ", rt, "%", sep="")
print("Tax deducted = Rs.", tax, sep="")
print("Your gross salary = Rs.", gr_sal, sep="")
