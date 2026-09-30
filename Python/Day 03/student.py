class Student : 

    def __init__(self, name, roll_no, cgpa, college):
        self.name = name 
        self.roll_no = roll_no
        self.cgpa = cgpa
        self.college = college

    def print_student_data(self) : 
        print(f"Name : {self.name}\nRoll Number : {self.roll_no}\nCGPA : {self.cgpa}\nCollege : {self.college}")