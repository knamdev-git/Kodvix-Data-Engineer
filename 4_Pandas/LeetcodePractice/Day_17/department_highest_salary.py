# Leetcode :
#  Problem 184 -> Write a solution to find employees who have the highest salary in each of the departments.
# Return the result table in any order.
# The result format is in the following example.



import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    # have to print the department name with their highest salary 
    # 1. grouping the department wise highest salary 
    highest_sal_dep = pd.merge(employee, department, how='left', left_on="departmentId", right_on="id", suffixes=('_emp', '_dep'))

    # highest_sal_dep['max_sal_dep'] = highest_sal_dep.groupby('departmentId')[['salary']].max() <---- it will put na in the colu…l_dep.groupby('departmentId')[['salary']].transform('max')
   
    ans = highest_sal_dep[['name_dep', 'name_emp', 'salary']][
            highest_sal_dep['salary'] == highest_sal_dep['max_sal_dep']
        ].rename(
            columns={
            'name_dep' : 'Department',
            'name_emp' : 'Employee',
            'salary' : 'Salary'
        })

    # print(highest_sal_dep[
    #     highest_sal_dep['salary'] == highest_sal_dep['max_sal_dep']
    # ])

    # print(ans)

    return ans
