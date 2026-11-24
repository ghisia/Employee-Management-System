class Employee:
    def __init__(self, employeeID, name, department, salary):
        self.employeeID = employeeID
        self.name = name
        self.department = department
        self.salary = salary

    def empInfo(self):
        print("ID:", self.employeeID)    
        print("Name:", self.name)
        print("Department:", self.department)
        print("Monthly Salary:", self.salary)

    def annualSalary(self):
        amount = self.salary * 12
        return amount

    def getSalary(self):
        print(f"Annual salary: {self.annualSalary()}")
        
        

    def increaseSalary(self, percentage):
        self.salary += self.salary * percentage / 100
        print("After 10% salary increase:")
        print(f"New Monthly Salary: {round(self.salary)}")



em = Employee(101, "Gigi", "Software E", 500000)

em.empInfo()
em.annualSalary()
em.getSalary()
em.increaseSalary(10)
