class employee:
    def __init__(self) -> None:
        pass
        self.name=""
        self.id=""
        self.salary=0
        self.dept=""
    
    def read(self):
        self.name=input("Enter the name: ")
        self.id=input("Enter the employee id: ")
        self.salary=int(input("Enter the employee salary: "))
        self.dept=input("Enter the employee department: ")

    def outtput(self):
        print("\n")
        print("Id of the employer is: ",self.id)
        print("Name of the employee is: ",self.name)
        print("Salary of the employee is: ",self.salary)
        print("Department of the employee is: ",self.dept)

    def updatesal(self):
        id=input("Enter the id to update the salary: ")
        if id==self.id:
             print("\n")
             self.salary=int(input("Enter the updated salary of the employee: "))
             print("The update salary of the employee is: ",self.salary)
        else:
            print("Invalid ID!")
            exit(0)

e = employee()
e.read()
e.outtput()
e.updatesal()

