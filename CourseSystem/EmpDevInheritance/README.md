Course & Premium Course System
Build a simple online learning platform using inheritance.
Use this structure
Course
|
PremiumCourse

The Course class should contain course name, instructor, duration, and price.
Add methods such as
show_course_details()
calculate_discount()

PremiumCourse should inherit from Course and add attributes such as mentor support and live sessions.
Use a class variable to count how many courses have been created and a class method to return the course count.
This task should demonstrate how a real EdTech platform can model courses using OOP.

Sample Input: 

pc1 = PremiumCourse("Advanced AI", "Raju", "6 months", 30000, 'yes', 'yes')
pc2 = PremiumCourse("AI", "Raju", "6 months", 30000, 'yes', 'yes')
pc3 = PremiumCourse("Devops", "Raju", "6 months", 30000, 'yes', 'yes')
pc4 = PremiumCourse("Python", "Raju", "6 months", 20000)

Sample Output:

Course Details: 
Course name: Advanced AI
Instructor: Raju
Duration: 6 months
Price: 30000
Mentor Support: yes
Live Sessions: yes
The discount 30% applied to the course Advanced AI
Course Details: 
Course name: AI
Instructor: Raju
Duration: 6 months
Price: 30000
Mentor Support: yes
Live Sessions: yes
The discount 20% applied to the course AI
Course Details: 
Course name: Devops
Instructor: Raju
Duration: 6 months
Price: 30000
Mentor Support: yes
Live Sessions: yes
The discount 25% applied to the course Devops
Course Details: 
Course name: Python
Instructor: Raju
Duration: 6 months
Price: 20000
Mentor Support: no
Live Sessions: no
The discount 10% applied to the course Python
Total number of courses 4
