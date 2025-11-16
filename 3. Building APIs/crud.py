
from fastapi import FastAPI, HTTPException
from models import Employee
from typing import List


employee_db: List[Employee] = []     
# for now our db is an empty list of Employee type(defined in models)
# variable name, variable type, variable value


app = FastAPI()


#1. read all employees

@app.get('/employees', response_model=List[Employee])        
def read_employees():
    return employee_db

'''
returns like this Response:
[
  {"id": 1, "name": "John", "department": "IT", "age": 25},
  {"id": 2, "name": "Jane", "department": "HR", "age": 30}
]
'''



#2. read specific employee

@app.get('/employees/{id}', response_model=Employee)
def read_employee(id: int):
    for emp in employee_db:
        if emp.id == id:
            return emp  # Returns single Employee 
    raise HTTPException(status_code=404, detail="Employee not found")





#3. add an employee.    { using id as primary key }

@app.post('/employees', response_model=Employee)
def add_employee(new_emp: Employee):
    for emp in employee_db:
        if emp.id == new_emp.id:
            raise HTTPException(status_code=400, detail="Employee with this ID already exists")
    employee_db.append(new_emp)
    return new_emp




#4. update an employee

@app.put('/employees/{id}', response_model=Employee)
def update(id:int, updated_emp: Employee):
    for index, emp in enumerate(employee_db):
        if emp.id == id:
            employee_db[index] = updated_emp
            return updated_emp
    raise HTTPException(status_code=404, detail="Employee not found")

'''
NOTE:
NO need index earlier for reading because we were just returning the object. 
For updates, you need to modify the list, so index is required.
deletion is also an update operation.

if emp.id == id:
        emp = updated_emp  # Only changes local variable, not the list!

        
But for individual attribute updates, you can do:

for emp in employee_db:
    if emp.id == id:
        emp.name = updated_emp.name
        emp.department = updated_emp.department
        emp.age = updated_emp.age
        return emp
raise HTTPException(status_code=404, detail="Employee not found")

'''



#5. delete an employee

@app.delete('/employees/{id}', response_model=Employee)
def delete_employee(id: int):
    for index, emp in enumerate(employee_db):
        if emp.id == id:
            return employee_db.pop(index)
    raise HTTPException(status_code=404, detail="Employee not found")


'''
OR

@app.delete('/employees/{id}')  # No response_model (returns dict)
def delete_employee(id: int):
    for index, emp in enumerate(employee_db):
        if emp.id == id:
            del employee_db[index] 
            return {"message": "Employee deleted successfully"}  
    raise HTTPException(status_code=404, detail="Employee not found")  

'''


