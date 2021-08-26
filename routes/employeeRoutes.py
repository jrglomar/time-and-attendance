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
    employee = db.query(Employee).filter(Employee.active_status == 'Active').all()
    return {'employee': employee}

@router.get('/{id}')
def read(id: str, db: Session = Depends(get_db)):
    employee = db.query(Employee).filter(Employee.id == id).filter(Employee.active_status == 'Active').first()
    if not employee:
        raise HTTPException(404, 'Employee not found')
    return {'employee': employee}

@router.post('/')
def store(employee: CreateEmployee, db: Session = Depends(get_db)):
    to_store = Employee(
        user_id = employee.user_id,
        shift_type_id = employee.shift_type_id,
        employee_type_id = employee.employee_type_id,
        monday = employee.monday,
        tuesday = employee.tuesday,
        wednesday = employee.wednesday,
        thursday = employee.thursday,
        friday = employee.friday,
        saturday = employee.saturday,
        sunday = employee.sunday,
    )

    db.add(to_store)
    db.commit()
    
    return {'message': 'Employee stored successfully.'}

@router.put('/{id}')
def update(id: str, employee: CreateEmployee, db: Session = Depends(get_db)): 
    if not db.query(Employee).filter(Employee.id == id).update({
        'user_id': employee.user_id,
        'shift_type_id': employee.shift_type_id,
        'employee_type_id': employee.employee_type_id,
        'monday': employee.monday,
        'tuesday': employee.tuesday,
        'wednesday': employee.wednesday,
        'thursday': employee.thursday,
        'friday': employee.friday,
        'saturday': employee.saturday,
        'sunday': employee.sunday,
    }):
        raise HTTPException(404, 'User to update is not found')
    db.commit()
    return {'message': 'Employee updated successfully.'}

@router.put('/delete/{id}')
def remove(id: str,  db: Session = Depends(get_db)):
    if not db.query(Employee).filter(Employee.id == id).update({
        'active_status': "Inactive",
    }):
        raise HTTPException(404, 'Employee to delete is not found')
    db.commit()
    return {'message': 'Employee removed successfully.'}
