class Employee:
    empData = {}
def __init__(self):
    empId = int(input(&quot;Enter employee id: &quot;))
    empName = input(&quot;Enter employee name: &quot;)
    empAge = int(input(&quot;Enter employee age: &quot;))
    empAddress = input(&quot;Enter employee address: &quot;)
Employee.empData[empId] = [empName, empAge, empAddress]
def show_data(self):
    print(Employee.empData)
def seach_employee(self):
    empId = int(input(&quot;Enter the employee id you want to search: &quot;))
if empId in Employee.empData:
    print(Employee.empData[empId])
else:
print(&quot;Employee doesnot exists&quot;)
for i in range(5):
    emp = Employee()
    emp.show_data()
    emp.seach_employee()
