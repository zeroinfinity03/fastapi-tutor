
import models, schemas, crud
from database import engine, SessionLocal, Base

from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List

Base.metadata.create_all(bind=engine)

app = FastAPI()


# apis se we establish a connection to the DB within the Session.
# So there is a dependency b/w our apis and DB
# and we need to specify that dependency.
def get_db():
    db = SessionLocal()
    try:
        yield db  # if everything goes well, ye Session object hum api endpoint ko de denge.
    finally:
        db.close()




# endpoints
# 1. create an employee here we will return the created employee
@app.post('/employees', response_model=schemas.EmployeeOut)   
def create_employee(employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    return crud.create_employee(db, employee)



# 2. get all employees
@app.get('/employees', response_model=List[schemas.EmployeeOut])
def get_employees(db: Session = Depends(get_db)):
    return crud.get_employees(db)



# 3. get specific employee
@app.get('/employees/{emp_id}', response_model=schemas.EmployeeOut)
def get_employee(emp_id: int, db: Session = Depends(get_db)):
    employee = crud.get_employee(db, emp_id)
    if employee is None:
        raise HTTPException(status_code=404, detail='Employee Not Found')
    return employee



# 4. update an employee
@app.put('/employees/{emp_id}', response_model=schemas.EmployeeOut)
def update_employee(emp_id: int, employee: schemas.EmployeeUpdate, db: Session = Depends(get_db)):
    db_employee = crud.update_employee(db, emp_id, employee)
    if db_employee is None:
        raise HTTPException(status_code=404, detail='Employee Not Found')
    return db_employee



# 5. delete an employee
@app.delete('/employees/{emp_id}', response_model=dict)
def delete_employee(emp_id: int, db: Session = Depends(get_db)):
    employee = crud.delete_employee(db, emp_id)
    if employee is None:
        raise HTTPException(status_code=404, detail='Employee Not Found')
    # return employee
    return {'detail': 'Employee Deleted'}





