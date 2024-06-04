from employee import Employee, salaryEmployee, hourlyEmployee, commissionEmployee

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

    employee1 = salaryEmployee("Charlie", "Dog", 100000)
    myCompany.addEmployee(employee1)

    employee2 = hourlyEmployee("Maya", "Dog", 40, 50)
    myCompany.addEmployee(employee2)

    employee3 = commissionEmployee("Auggie", "Dog", 50000, 5, 50)
    myCompany.addEmployee(employee3)

    myCompany.displayEmployees()
    myCompany.printChecks()

main()