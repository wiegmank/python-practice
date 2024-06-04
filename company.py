from employee import Employee

class Company:
    def __init__(self):
        self.employees = []

    def addEmployee(self, newEmployee):
        self.employees.append(newEmployee)

    def displayEmployees(self):
        print("Current Employees:")
        for i in self.employees:
            print(i.firstName, i.lastName)
        print("~~~~~~~~~~~~~~~~~~~~~~~~")

    def printChecks(self):
        print("PAYING EMPLOYEES...")
        for i in self.employees:
            print(i.firstName, i.lastName)
            print(f"Amount: $ {i.calculatePaycheck():,.2f}")
            print("####################")
        

def main():
    myCompany = Company()

    employee1 = Employee("Charlie", "Dog", 100000)
    myCompany.addEmployee(employee1)

    employee2 = Employee("Maya", "Dog", 90000)
    myCompany.addEmployee(employee2)

    employee3 = Employee("Auggie", "Dog", 80000)
    myCompany.addEmployee(employee3)

    myCompany.displayEmployees()
    myCompany.printChecks()

main()