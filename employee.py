class Employee:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

class hourlyEmployee(Employee):
    def __init__(self, firstName, lastName, weeklyHours, hourlyRate):
        super().__init__(firstName, lastName)
        self.weeklyHours = weeklyHours
        self.hourlyRate = hourlyRate
    
    def calculatePaycheck(self):
        return self.weeklyHours * self.hourlyRate

class salaryEmployee(Employee):
    def __init__(self, firstName, lastName, salary):
        super().__init__(firstName, lastName)
        self.salary = salary
    
    def calculatePaycheck(self):
        return self.salary/52
    
class commissionEmployee(salaryEmployee):
    def __init__(self, firstName, lastName, salary, numSales, commissionRate):
        super().__init__(firstName, lastName, salary)
        self.numSales = numSales
        self.commissionRate = commissionRate

    def calculatePaycheck(self):
        regularSalary = super().calculatePaycheck()
        totalBonus = self.numSales * self.commissionRate
        return regularSalary + totalBonus
