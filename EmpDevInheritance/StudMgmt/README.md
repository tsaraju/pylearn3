Create a base class called Employee.
It should contain employee ID, name, salary, and department, along with a method display_details().
Now create a child class

Employee
|
Developer

Developer should inherit from Employee and contain additional information such as programming language and experience.
Create at least 3 Employee/Developer objects and demonstrate how the child class can access functionality from the parent class.
Expected concepts: Parent class, child class, inheritance, object creation.

Sample Input: 
d1 = Developer("Raju", 45652, 30000, 'Devops', 'Python', 5)
d2 = Developer("Rani", 35650, 40000, 'ML', 'Python', 4)
d3 = Developer("Ramu", 49558, 25000, 'DL', 'Python', 3)

Sample Output:
Employee Details: 
Employee ID: Raju
Employee Name: 45652
Employee Salary: 30000
Employee Department: Devops
Programming Languages: Python
Experience: 5
Employee Details: 
Employee ID: Rani
Employee Name: 35650
Employee Salary: 40000
Employee Department: ML
Programming Languages: Python
Experience: 4
Employee Details: 
Employee ID: Ramu
Employee Name: 49558
Employee Salary: 25000
Employee Department: DL
Programming Languages: Python
Experience: 3
