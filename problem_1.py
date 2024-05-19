# department highest salary leetcode 184

#longer method
import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    #creating empty salary dictionary
    salaryDictionary = {}
    for i in range(len(employee)):
        salary=employee['salary'][i]
        d_id= employee['departmentId'][i]
        if d_id in salaryDictionary:
            if salary > salaryDictionary[d_id]:
                salaryDictionary[d_id]=salary
        else:
            salaryDictionary[d_id] = salary
    
    #creating empty department dictionary        
    deptDictioanry = {}
    for i in range(len(department)):
        d_id = department['id'][i]
        name = department['name'][i]
        deptDictioanry[d_id]=name
        
    #empty list
    result=[]
    for i in range(len(employee)):
        d_id = employee['departmentId'][i]
        name = employee['name'][i]
        salary = employee['salary'][i]
        if salaryDictionary[d_id] == salary:
            result.append([d_id, name, salary])
            
    #renaming the id in result to name of department
    for element in result:
        d_id = element[0]
        element [0] = deptDictioanry [d_id]
        
    #returning dataframe
    return pd.DataFrame(result, columns=['Department', 'Employee', 'Salary'])


#Other short method using merge

import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    df= employee.merge(department, left_on='departmentId', right_on='id', how = 'left')
    max_salary= df.groupby('name_y')['salary'].transform('max')
    df= df[df['salary'] == max_salary]
    return df[['name_y', 'name_x', 'salary']].rename(columns = {'name_y' : 'department', 'name_x': 'Employee'})