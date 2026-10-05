from student import Student 

ram = Student("ram", 123, 7.77, "Bansal")
mike = Student("Mike Leonheart", 221, 7.2, "Bansal")
agiris = Student("Agiris Jackson", 213, 8.9, "Bansal")

Student.course = "Bsc"
student_lists = [ram, mike, agiris]

for each_student_info in student_lists : 
    print(f"{each_student_info.name}\n Roll Number : {each_student_info.roll_no}\n CGPA : {each_student_info.cgpa}\n Course : {each_student_info.course}")
    print(" ")
