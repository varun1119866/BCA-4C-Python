class StudentDetails:
    mydict = {}
def get_info(self):
    self.rollNo = input(&quot;Enter student rollNo: &quot;)
    self.name = input(&quot;Enter student name: &quot;)
    StudentDetails.mydict[self.rollNo] = [self.name]
class StudentMoreDetails(StudentDetails):
    def get_more_info(self):
        super().get_info()
        self.age = int(input(&quot;Enter student age: &quot;))
        self.stream = input(&quot;Enter student stream: &quot;)
        self.emailId = input(&quot;Enter student emailId: &quot;)
        self.contactNo = input(&quot;Enter student ContactNo: &quot;)
        StudentDetails.mydict[self.rollNo].append(self.age)
        StudentDetails.mydict[self.rollNo].append(self.stream)
        StudentDetails.mydict[self.rollNo].append(self.emailId)
        StudentDetails.mydict[self.rollNo].append(self.contactNo)
def show_student_data(self):
        print(StudentDetails.mydict)
        student = StudentMoreDetails()
        student.get_more_info()
        student.show_student_data()
