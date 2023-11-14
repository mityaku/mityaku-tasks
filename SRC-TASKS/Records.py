student1t=("Dave","Bloggs",18,True) #ordered

class student_record:
    def __init__(self):
        self.firstname = ""
        self.surname = ""
        self.age = 0
        self.registered = False


student2 = student_record()
student2.firstname = "Fred"
student2.surname = "Smith"
student2.age = 16
student2.registered = False

print(student2.firstname)
