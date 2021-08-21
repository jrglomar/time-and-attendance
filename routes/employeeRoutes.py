from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.employeeSchema import CreateEmployee
from models.employeeModel import Employee
from database import get_db


router = APIRouter(
    prefix='/time_and_attendance/api/employee',
    tags=['employee']
)

@router.get('/')
def all(db: Session = Depends(get_db)):
    users = db.query(Employee).all()
    return {'users': users}

@router.get('/{id}')
def read(id: str, db: Session = Depends(get_db)):
    user = db.query(Employee).filter(Employee.id == id).first()
    if not user:
        raise HTTPException(404, 'Employee not found')
    return {'user': user}

@router.post('/')
def store(employee: CreateEmployee, db: Session = Depends(get_db)):
    to_store = Employee(
        user_type_id = employee.user_type_id,
        user_profile_id = employee.user_profile_id,
    )

    db.add(to_store)
    db.commit()
    
    return {'message': 'Employee stored successfully.'}

@router.put('/{id}')
def update(id: str, employee: CreateEmployee, db: Session = Depends(get_db)): 
    if not db.query(Employee).filter(Employee.id == id).update({
        'name': employee.name,
        'age': employee.age
    }):
        raise HTTPException(404, 'User to update is not found')
    db.commit()
    return {'message': 'Employee updated successfully.'}

@router.delete('/{id}')
def remove(id: str, db: Session = Depends(get_db)):
    if not db.query(Employee).filter(Employee.id == id).delete():
        raise HTTPException(404, 'User to delete is not found')
    db.commit()
    return {'message': 'Employee removed successfully.'}

