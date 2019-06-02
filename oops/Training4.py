class Training:
    institute_name = "XYZ Tech"

    def __init__(self,a,b):
        self.sid = a
        self.name = b
        self.x = 10

    def f1(self):
        print(self.institute_name)

    def print_student_details(self):
        print("The student details are :"
              " \n Sid : ",self.sid,"\n name : ",self.name)

t = Training(1001,'Dharani')
t2 = Training(1002,'Supriya')

t2.print_student_details()