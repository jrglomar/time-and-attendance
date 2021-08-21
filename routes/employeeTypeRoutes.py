from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.employeeTypeSchema import CreateEmployeeType
from models.employeeTypeModel import EmployeeType
from database import get_db
from datetime import date


router = APIRouter(
    prefix='/time_and_attendance/api/employeetype',
    tags=['employeetype']
)

@router.get('/')
def all(db: Session = Depends(get_db)):
    employeetype = db.query(EmployeeType).filter(EmployeeType.active_status == 'Active').all()
    return {'employeetype': employeetype}

@router.get('/{id}')
def read(id: str, db: Session = Depends(get_db)):
    employeetype = db.query(EmployeeType).filter(EmployeeType.id == id).first()
    if not employeetype:
        raise HTTPException(404, 'Employee type not found')
    return {'employeetype': employeetype}

@router.post('/')
def store(employeetype: CreateEmployeeType, db: Session = Depends(get_db)):
    to_store = EmployeeType(
        title = employeetype.title,
    )

    db.add(to_store)
    db.commit()
    
    return {'message': 'Employee Type stored successfully.'}

@router.put('/{id}')
def update(id: str, employeetype: CreateEmployeeType, db: Session = Depends(get_db)): 
    if not db.query(EmployeeType).filter(EmployeeType.id == id).update({
        'title': employeetype.title,
    }):
        raise HTTPException(404, 'Employee to update is not found')
    db.commit()
    return {'message': 'Employee Type updated successfully.'}

@router.put('/delete/{id}')
def remove(id: str,  db: Session = Depends(get_db)):
    if not db.query(EmployeeType).filter(EmployeeType.id == id).update({
        'active_status': "Inactive",
    }):
        raise HTTPException(404, 'Employee type to delete is not found')
    db.commit()
    return {'message': 'Employee type removed successfully.'}

