'''
marks = np.array([45, 78, 32, 90, 66, 55, 88])
'''
import numpy as np 

marks = np.array([45, 78, 32, 90, 66, 55, 88])

# finding average marks 

print(np.mean(marks))
print(np.max(marks))
print(np.min(marks))

# marks which is greater then 60 
A_rank_student = marks[marks>60]
print(A_rank_student)

low_student_scoring = marks[marks<40]
print(low_student_scoring)