class student:
    # Class variable to track total students
    total_students = 0

    def __init__(self, name, email, studid, course, marks):
        self.name = name
        self.email = email
        self.studid = studid
        self.course = course
        self.marks = marks

        # Increment when the object is created
        student.total_students += 1

    # Display Student Details
    def stud_data(self):
        print("Student Details:")
        print(f"Student Name: {self.name}")
        print(f"Student Email: {self.email}")
        print(f"Student ID: {self.studid}")
        print(f"Student Course: {self.course}")
        print(f"Student Marks: {self.marks}")

    # Update marks of Student                                    
    def update_marks(self, new_marks):
        self.marks = new_marks
        return self.marks

    # Calculate average marks
    def calc_avg(self):
        if len(self.marks) == 0:
            return 0
        return sum(self.marks) / len(self.marks)

    # Class method
    @classmethod
    def get_total_students(cls):
        return student.total_students

# Students
student1 = student("Raju", "raju@yahoo.com", 12345, "M.Tech", [90,87,96,79,94])
student1.stud_data()
update_marks = student1.update_marks([78,99,95,97,89])
print(f"After updating the marks: {update_marks}")
avg = student1.calc_avg()
print(f"Average of the marks: {avg}")

student2 = student("Rani", "rani@gmail.com", 22349, "M.Sc", [80,77,86,89,74])
student2.stud_data()
update_marks = student2.update_marks([88,69,75,77,79])
print(f"After updating the marks: {update_marks}")
avg = student2.calc_avg()
print(f"Average of the marks: {avg}")

student3 = student("Ramu", "ramu@gmail.com", 52347, "M.A", [70,67,86,74,88])
student3.stud_data()
update_marks = student3.update_marks([68,89,75,87,84])
print(f"After updating the marks: {update_marks}")
avg = student3.calc_avg()
print(f"Average of the marks: {avg}")

# Total number of students
print("Total number of students: ", student.get_total_students())