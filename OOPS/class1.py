class Student:
    """docstring for ClassName"""
    clg = "KLU"

    def __init__(self, id, name, course):
        self.id = id
        self.name = name
        self.course = course

    def display(self):
        print(f"This is {self.id}")
        print(f"This is {self.name}")
        print(f"This is {self.course}")


s1 = Student(1234, "Vinay", "PFSD")

print(s1)
s1.display()
print(Student.clg)
