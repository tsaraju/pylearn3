class Course:
    # Class variable to count all courses
    courses = 0

    def __init__(self, course_name, instructor, duration, price):
        self.course_name = course_name
        self.instructor = instructor
        self.duration = duration
        self.price = price

        Course.courses += 1

    def show_course_details(self):
        print("Course Details: ")
        print(f"Course name: {self.course_name}")
        print(f"Instructor: {self.instructor}")
        print(f"Duration: {self.duration}")
        print(f"Price: {self.price}")

    def calculate_discount(self):
        if self.course_name == "Advanced AI":
            self.disc = 30
        elif self.course_name == "Devops":
            self.disc = 25
        elif self.course_name == "AI":
            self.disc = 20
        else:
            self.disc = 10

        print(f"The discount {self.disc}% applied to the course {self.course_name}")

    @classmethod
    def course_count(cls):
        return cls.courses

class PremiumCourse(Course):
    def __init__(self, course_name, instructor, duration, price, mentor_support='no', live_sessions='no'):
        super().__init__(course_name, instructor, duration, price)
        self.mentor_support = mentor_support
        self.live_sessions = live_sessions

    def show_course_details(self):
        super().show_course_details()   # Parent method
        print(f"Mentor Support: {self.mentor_support}")
        print(f"Live Sessions: {self.live_sessions}")

# Demo
pc1 = PremiumCourse("Advanced AI", "Raju", "6 months", 30000, 'yes', 'yes')
pc1.show_course_details()
pc1.calculate_discount()

pc2 = PremiumCourse("AI", "Raju", "6 months", 30000, 'yes', 'yes')
pc2.show_course_details()
pc2.calculate_discount()

pc3 = PremiumCourse("Devops", "Raju", "6 months", 30000, 'yes', 'yes')
pc3.show_course_details()
pc3.calculate_discount()

pc4 = PremiumCourse("Python", "Raju", "6 months", 20000)
pc4.show_course_details()
pc4.calculate_discount()

print("Total number of courses", PremiumCourse.course_count())