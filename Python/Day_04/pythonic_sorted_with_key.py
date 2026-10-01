import sys
sys.path.append("/home/anjali/GitHub/Kodvix-Data-Engineer/Python")

from Day_03.student import Student
# here the concept of sorted () in python 

list = ["Aaaaaaaaaaaa", "BBB", "CC", "D"]

# print(sorted(list, key=len)) #based on each key length it will sort the list 

# syntax sorted(iterabl, key="required condition")  
s1 = Student("Mikasa", 1, 8.21, "XYZ")
s2 = Student("Arvin", 2, 4.02, "XYZ")
s3 = Student("Todoroki", 3, 7.21, "XYZ")


students_list = [s1,s2,s3]

sorted_students = sorted(students_list, key=lambda s : s.cgpa, reverse=True)
print([f"{student.name} {student.cgpa}" for student in sorted_students])
