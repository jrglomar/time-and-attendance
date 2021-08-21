from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.attendanceSchema import CreateAttendance
from models.attendanceModel import Attendance
from database import get_db


router = APIRouter(
    prefix='/time_and_attendance/api/attendance',
    tags=['attendance']
)

@router.get('/')
def all(db: Session = Depends(get_db)):
    attendance = db.query(Attendance).all()
    return {'attendance': attendance}

@router.get('/{id}')
def read(id: str, db: Session = Depends(get_db)):
    attendance = db.query(Attendance).filter(Attendance.id == id).first()
    if not attendance:
        raise HTTPException(404, 'Attendance not found')
    return {'attendance': attendance}

@router.post('/')
def store(attendance: CreateAttendance, db: Session = Depends(get_db)):
    to_store = Attendance(
        employee_id = attendance.employee_id,
        shift_type_id = attendance.shift_type_id,
        time_in_id = attendance.time_in_id,
        time_out_id = attendance.time_out_id,
        hours_worked = attendance.hours_worked,
    )

    db.add(to_store)
    db.commit()
    
    return {'message': 'Attendance stored successfully.'}

@router.put('/{id}')
def update(id: str, attendance: CreateAttendance, db: Session = Depends(get_db)): 
    if not db.query(Attendance).filter(Attendance.id == id).update({
        'name': attendance.name,
        'age': attendance.age
    }):
        raise HTTPException(404, 'User to update is not found')
    db.commit()
    return {'message': 'Attendance updated successfully.'}

@router.delete('/{id}')
def remove(id: str, db: Session = Depends(get_db)):
    if not db.query(Attendance).filter(Attendance.id == id).delete():
        raise HTTPException(404, 'User to delete is not found')
    db.commit()
    return {'message': 'Attendance removed successfully.'}

