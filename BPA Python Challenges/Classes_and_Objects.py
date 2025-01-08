class Student:
    def __init__(self, name, grade, percentage):
        self.name = name
        self.grade = grade
        self.percentage = percentage

    def display_info(self):
        return f"I am {self.name} and I'm in {self.grade}th grade! I have a {self.percentage} grade percentage. I am passing!"

Student1 = Student("John", 10, 72)
Student2 = Student("Jack", 11, 89)

print(Student1.display_info())
print(Student2.display_info())

#I first created the student class and created a name object, grade object, and percentage object. I then made a function to display the info to the reader that would tell you their name, grade level, and their grade percentage currently. Then I made two objects from the class, both of the students! They contained their names, grade, and percentage. I then printed their info and that they passed.