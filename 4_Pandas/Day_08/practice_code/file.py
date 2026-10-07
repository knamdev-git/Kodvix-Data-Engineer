import pandas as pd 

class Data : 
    employees = pd.DataFrame({
    "employee_id": [101, 102, 103, 104, 105, 106, 107, 108],
    "name": ["Rahul", "Priya", "Amit", "Neha", "Raj", "Sneha", "Vikas", "Anjali"],
    "department_id": [1, 2, 1, 3, 2, 3, 1, 2],
    "salary": [45000, 52000, 48000, 60000, 55000, None, 47000, 52000],
    "experience": [2, 3, 2, 5, 4, 6, None, 3],
    "city": ["Indore", "Delhi", "Pune", "Mumbai", "Delhi", "Pune", "Indore", "Delhi"]
})

    projects = pd.DataFrame({
    "employee_id": [101, 102, 103, 105, 105, 108, 109],
    "project": ["E-Commerce", "Recruitment", "Banking", "CRM", "Analytics", "ERP", "Cloud"],
    "hours": [120, 100, 150, 90, 110, 130, 80]
})

    departments = pd.DataFrame({"department_id": [1, 2, 3, 4],    "department": ["IT", "HR", "Finance", "Marketing"]})

