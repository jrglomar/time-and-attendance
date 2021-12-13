from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.employeeStatusSchema import CreateEmployeeStatus
from models.employeeStatusModel import EmployeeStatus
from database import get_db
from datetime import date


router = APIRouter(
    prefix='/time_and_attendance/api/employeestatus',
    tags=['employeestatus']
)

@router.get('/')
def all(db: Session = Depends(get_db)):
    employeestatus = db.query(EmployeeStatus).filter(EmployeeStatus.active_status == 'Active').all()
    return {'employeestatus': employeestatus}

@router.get('/{id}')
def read(id: str, db: Session = Depends(get_db)):
    employeestatus = db.query(EmployeeStatus).filter(EmployeeStatus.id == id).first()
    if not employeestatus:
        raise HTTPException(404, 'Employee status not found')
    return {'employeestatus': employeestatus}

@router.post('/')
def store(employeestatus: CreateEmployeeStatus, db: Session = Depends(get_db)):
    to_store = EmployeeStatus(
        title = employeestatus.title,
        number_of_days = employeestatus.number_of_days,
    )

    db.add(to_store)
    db.commit()
    
    return {'message': 'Employee Status stored successfully.'}

@router.put('/{id}')
def update(id: str, employeestatus: CreateEmployeeStatus, db: Session = Depends(get_db)): 
    if not db.query(EmployeeStatus).filter(EmployeeStatus.id == id).update({
        'title': employeestatus.title,
        'number_of_days': employeestatus.number_of_days
    }):
        raise HTTPException(404, 'Employee to update is not found')
    db.commit()
    return {'message': 'Employee Type updated successfully.'}

@router.put('/delete/{id}')
def remove(id: str,  db: Session = Depends(get_db)):
    if not db.query(EmployeeStatus).filter(EmployeeStatus.id == id).update({
        'active_status': "Inactive",
    }):
        raise HTTPException(404, 'Employee type to delete is not found')
    db.commit()
    return {'message': 'Employee type removed successfully.'}

