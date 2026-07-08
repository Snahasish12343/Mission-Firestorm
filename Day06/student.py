class Student:
    def __init__(self, name, major, gpa):
        self.name = name
        self.major = major
        self.gpa = gpa

    def honor(self):
        if self.gpa >= 3.2:
            return True
        else:
            return False
        