Build a mini Super30 Learning Platform.

Students should design classes such as
User
|
+---- Student
|
+---- Mentor

The User class can contain name, email, and user ID.
Student should contain course name and completed assignments.
Mentor should contain expertise and number of students assigned.
Students must use at least one class variable, one class method, one static method, inheritance, multiple objects, constructors, and instance methods.
Example functionality can include registering students, assigning a course, submitting an assignment, displaying student information, displaying mentor information, and counting the total number of users.

Sample Input:

# -------------------------------
# Create Student objects
# -------------------------------

s1 = Student(
    "Raju",
    "raju@gmail.com",
    "S101",
    "Python Programming",
    2
)

s2 = Student(
    "Rani",
    "rani123@gmail.com",
    "S102",
    "Data Science",
    3
)


# -------------------------------
# Create Mentor objects
# -------------------------------

m1 = Mentor(
    "Dr. Ramu",
    "ramu@gmail.com",
    "M201",
    "Python"
)

m2 = Mentor(
    "Dr. Ravi",
    "ravi@gmail.com",
    "M202",
    "Machine Learning"
)

Sample Output:
Raju has been assigned to mentor Dr. Ramu.
Rani has been assigned to mentor Dr. Ramu.
Rani has been assigned to mentor Dr. Ravi.

--- Student Information ---
User Information
User name: Raju
User email: raju@gmail.com
User userID: S101
Student course_name: Python Programming
Student completed_assignments: 5

--- Assign Course ---
Raju has been assigned to Advanced Python.

--- Submit Assignment ---
Raju submitted an assignment. Total completed: 6

--- Updated Student Information ---
User Information
User name: Raju
User email: raju@gmail.com
User userID: S101
Student course_name: Advanced Python
Student completed_assignments: 5

--- Total number of assignments ---

--- Mentor Information ---
User Information
User name: Dr. Ramu
User email: ramu@gmail.com
User userID: M201
Expertise: Python
Number of Students: 2
Students:
  - Raju
  - Rani

--- Mentor Information ---
User Information
User name: Dr. Ravi
User email: ravi@gmail.com
User userID: M202
Expertise: Machine Learning
Number of Students: 1
Students:
  - Rani

--- Course Validation ---
True
False

--- Total Users ---
Total users: 4
