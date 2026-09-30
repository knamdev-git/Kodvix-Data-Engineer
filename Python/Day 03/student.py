class Student : 

# example of class variable too
    course = "Btech"

    def __init__(self, name, roll_no, cgpa, college):
        self.name = name 
        self.roll_no = roll_no
        self.cgpa = cgpa
        self.college = college

    def print_student_data(self) : 
        print(f"Name : {self.name}\nRoll Number : {self.roll_no}\nCGPA : {self.cgpa}\nCollege : {self.college}")


class My_Math : 

    def __init__(self, a, b):
        self.a = a 
        self.b = b

    def multiplication(self, a,b): 
        return self.a * self.b
        
    @staticmethod
    def add(a,b) : 
        return a + b

