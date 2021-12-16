from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.attendanceSchema import CreateAttendance, GetAttendanceReport, UpdateAttendanceOut, GetAttendance, GetAttendanceOne
from models.attendanceModel import Attendance
from database import get_db
from datetime import datetime
from sqlalchemy import extract

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


@router.get('/datatable/{id}')
def read(id: str, db: Session = Depends(get_db)):
    attendance = db.query(Attendance).filter(Attendance.employee_id == id).all()
    return {'attendance': attendance}

@router.post('/')
def store(attendance: CreateAttendance, db: Session = Depends(get_db)):
    to_store = Attendance(
        employee_id = attendance.employee_id,
        time_in_id = attendance.time_in_id,
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


@router.put('/update_timeout/{id}')
def update(id: str, attendance: UpdateAttendanceOut, db: Session = Depends(get_db)): 
    if not db.query(Attendance).filter(Attendance.time_in_id == id).update({
        'time_out_id': attendance.time_out_id
    }):
        raise HTTPException(404, 'Attendance to update is not found')
    db.commit()
    return {'message': 'Attendance updated successfully.'}



@router.post('/reports/{id}')
def all(id: str, report: GetAttendanceReport, db: Session = Depends(get_db)):
    attendance = db.query(Attendance).filter(Attendance.employee_id == id).filter(Attendance.created_at >= report.start_date).filter(Attendance.created_at <= report.end_date).filter(Attendance.active_status == "Active").all()
    return {'attendance': attendance}


@router.post('/reports_all')
def all(report: GetAttendanceReport, db: Session = Depends(get_db)):
    attendance = db.query(Attendance).filter(Attendance.created_at >= report.start_date).filter(Attendance.created_at <= report.end_date).filter(Attendance.active_status == "Active").all()
    return {'attendance': attendance}

@router.post('/getAttendance')
def all(attendance: GetAttendance, db: Session = Depends(get_db)):
    
    attendance = db.query(Attendance).filter(Attendance.created_at >= attendance.start_date).filter(Attendance.created_at <= attendance.end_date).all()
    return {'attendance': attendance}

@router.post('/getAttendanceOne')
def all(attendance: GetAttendanceOne, db: Session = Depends(get_db)):
    
    attendance = db.query(Attendance).filter(Attendance.employee_id == attendance.employee_id).filter(Attendance.created_at >= attendance.start_date).filter(Attendance.created_at <= attendance.end_date).all()
    return {'attendance': attendance}

@router.get('/count/month/')
def count(db: Session = Depends(get_db)):
    today = datetime.today()
    count = db.query(Attendance).filter(extract('month', Attendance.created_at)==today.month).filter(extract('year', Attendance.created_at)==today.year).count()
    return {'count': count}

@router.get('/count/today/')
def count(db: Session = Depends(get_db)):
    today = datetime.today()
    count = db.query(Attendance).filter(extract('day', Attendance.created_at)==today.day).filter(extract('month', Attendance.created_at)==today.month).filter(extract('year', Attendance.created_at)==today.year).count()
    return {'count': count}

@router.post('/count/month/{id}')
def count(id: str, db: Session = Depends(get_db)):
    today = datetime.today()
    count = db.query(Attendance).filter(Attendance.employee_id == id).filter(extract('month', Attendance.created_at)==today.month).filter(extract('year', Attendance.created_at)==today.year).count()
    return {'count': count}

@router.post('/count/today/{id}')
def count(id: str, db: Session = Depends(get_db)):
    today = datetime.today()
    count = db.query(Attendance).filter(Attendance.employee_id == id).filter(extract('day', Attendance.created_at)==today.day).filter(extract('month', Attendance.created_at)==today.month).filter(extract('year', Attendance.created_at)==today.year).count()
    return {'count': count}