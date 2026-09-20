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
d1 = Developer(45652, "Raju", 30000, 'Devops', 'Python', 5)
d2 = Developer(35650, "Rani", 40000, 'ML', 'Python', 4)
d3 = Developer(49558, "Ramu", 25000, 'DL', 'Python', 3)

Sample Output:
Employee Details: 
Employee ID: 45652
Employee Name: Raju
Employee Salary: 30000
Employee Department: Devops
Programming Languages: Python
Experience: 5
Employee Details: 
Employee ID: 35650
Employee Name: Rani
Employee Salary: 40000
Employee Department: ML
Programming Languages: Python
Experience: 4
Employee Details: 
Employee ID: 49558
Employee Name: Ramu
Employee Salary: 25000
Employee Department: DL
Programming Languages: Python
Experience: 3