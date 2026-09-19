class Employee:

    def __init__(self, empid, name, salary, dept):
        self.empid = empid
        self.name = name
        self.salary = salary
        self.dept = dept

class Developer(Employee):

    def __init__(self, empid, name, salary, dept, proglan, exp):
        super().__init__(empid, name, salary, dept)
        self.proglan = proglan
        self.exp = exp

    def display_details(self):
        print("Employee Details: ")
        print(f"Employee ID: {self.empid}")
        print(f"Employee Name: {self.name}")
        print(f"Employee Salary: {self.salary}")
        print(f"Employee Department: {self.dept}")
        print(f"Programming Languages: {self.proglan}")
        print(f"Experience: {self.exp}")
        
d1 = Developer("Raju", 45652, 30000, 'Devops', 'Python', 5)
d1.display_details()

d2 = Developer("Rani", 35650, 40000, 'ML', 'Python', 4)
d2.display_details()

d1 = Developer("Ramu", 49558, 25000, 'DL', 'Python', 3)
d1.display_details()
