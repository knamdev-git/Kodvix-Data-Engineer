# 177. Nth Highest Salary
# import pandas as pd

# def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
#     sal = employee[['salary']].drop_duplicates().sort_values(by='salary',ascending=False)
#     sol = 0 
#     if N <= 0 or N > len(employee) : 
#         return pd.DataFrame({f"getNthHighestSalary({N})" : [None]})
    
    
#     sol = sal.iloc[[N-1]]['salary']

#     return pd.DataFrame({
#         f"getNthHighestSalary({N})" : [sol]}
#     )

# Leetcode ques : 177. Nth Highest Salary

import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    ans = employee['salary'].drop_duplicates().nlargest(N)
    result = ans.iloc[N-1] if 0 < N <= len(ans) else None
    return pd.DataFrame({
        f"getNthHighestSalary({N})" : [result]
    })