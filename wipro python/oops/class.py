# class is a blue print or a template
# which describes the state/ behaviour of its object
# data is put in variables
# behaviour is put in the function
class student:
    # data or the properties
    studentname = "Ravi"
    studentid = 677887
    # self is used to access the attributes of the class we have defined
    # it is automatically loaded
    # self represents the instance of the class
    # create a function to access the data
    def displaystudentdetails(self):
        print(f"the student name is {self.studentname} and student id is {self.studentid}")
# create the object of the class
a = student()
a.displaystudentdetails()


# wap to create a class for an employee with your data empid, empname,emp address, employeedept, create a function to display the data
class employee:
    empid = ""
    empname = ""
    empaddress = ""
    empdept = ""
    def emp_input(self):
        self.empid = input("enter the emp id")
        self.empname = input("enter the emp name")
        self.empaddress = input("enter the emp address")
        self.empdept = input("enter the emp dept")
    def print_details(self):
        print(f"the emp name is {self.empid} of emp id {self.empname} emp address is {self.empaddress} and dept is {self.empdept}")

emp1 = employee()
emp1.emp_input()
emp2 = employee()
emp2.emp_input()
emp1.print_details()
emp2.print_details()