class User:
    # Class variable to count total number of users
    users_count = 0

    # Constructor
    def __init__(self, name, email, userID):
        self.name = name
        self.email = email
        self.userID = userID

        User.users_count += 1

    # Instance method
    def display_info(self):
        print("User Information")
        print(f"User name: {self.name}")
        print(f"User email: {self.email}")
        print(f"User userID: {self.userID}")

    @classmethod
    def total_users(cls):
        return cls.users_count

class Student(User):
    # Class variable to catpure completed assignments
    completed_assignments = 0

    # Constructor
    def __init__(self, name, email, userID, course_name, assign):
        super().__init__(name, email, userID)
        self.course_name = course_name
        self.assign = assign

        Student.completed_assignments += self.assign

    # Instance method
    def display_student_info(self):
        self.display_info()
        print(f"Student course_name: {self.course_name}")
        print(f"Student completed_assignments: {Student.completed_assignments}")

    # Instance method
    def assign_course(self, course_name):
        self.course_name = course_name
        print(f"{self.name} has been assigned to {course_name}.")

    # Instance method
    def submit_assignment(self):
        self.completed_assignments += 1
        print(f"{self.name} submitted an assignment. Total completed: {self.completed_assignments}")
    
    # Class method                           
    @classmethod
    def total_assignments(cls):
        return cls.completed_assignments

    # Static method
    @staticmethod
    def is_valid_course(course_name):
        return course_name.strip() != ""

class Mentor(User):
    # Constructor
    def __init__(self, name, email, userID, expertise, students=None):
          super().__init__(name, email, userID)
          self.expertise = expertise

          # Store assigned students in a list
          if students is None:
            self.students = []
          else:
            self.students = students

    # Instance method
    def assign_student(self, student):
        self.students.append(student)
        print(
            f"{student.name} has been assigned to mentor "
            f"{self.name}."
        )

    # Instance method
    def display_mentor_info(self):
        self.display_info()
        print(f"Expertise: {self.expertise}")
        print(f"Number of Students: {len(self.students)}")

        if self.students:
            print("Students:")
            for student in self.students:
                print(f"  - {student.name}")


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


# -------------------------------
# Assign students to mentors
# -------------------------------

m1.assign_student(s1)
m1.assign_student(s2)

m2.assign_student(s2)


# -------------------------------
# Student functionality
# -------------------------------

print("\n--- Student Information ---")
s1.display_student_info()

print("\n--- Assign Course ---")
s1.assign_course("Advanced Python")

print("\n--- Submit Assignment ---")
s1.submit_assignment()

print("\n--- Updated Student Information ---")
s1.display_student_info()

print("\n--- Total number of assignments ---")
Student.total_assignments()


# -------------------------------
# Mentor functionality
# -------------------------------

print("\n--- Mentor Information ---")
m1.display_mentor_info()

print("\n--- Mentor Information ---")
m2.display_mentor_info()


# -------------------------------
# Static method
# -------------------------------

print("\n--- Course Validation ---")
print(Student.is_valid_course("Python Programming"))
print(Student.is_valid_course(""))


# -------------------------------
# Class method
# -------------------------------

print("\n--- Total Users ---")
print("Total users:", User.total_users())
