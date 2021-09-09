from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.missedTimeSchema import CreateMissedTime, UpdateMissedTime
from models.missedTimeModel import MissedTime
from database import get_db


router = APIRouter(
    prefix='/time_and_attendance/api/missed_time',
    tags=['missed_time']
)

@router.get('/')
def all(db: Session = Depends(get_db)):
    missed_time = db.query(MissedTime).filter(MissedTime.active_status == 'Active').all()
    return {'missed_time': missed_time}

@router.get('/employee/{id}')
def employee(id: str, db: Session = Depends(get_db)):
    missed_time = db.query(MissedTime).filter(MissedTime.employee_id == id).filter(MissedTime.active_status == 'Active').all()
    return {'missed_time': missed_time}

@router.get('/{id}')
def read(id: str, db: Session = Depends(get_db)):
    missed_time = db.query(MissedTime).filter(MissedTime.id == id).first()
    if not missed_time:
        raise HTTPException(404, 'Missed Time not found')
    return {'missed_time': missed_time}

@router.post('/')
def store(missed_time: CreateMissedTime, db: Session = Depends(get_db)):
    to_store = MissedTime(
        date = missed_time.date,
        time_log = missed_time.time_log,
        time_log_type = missed_time.time_log_type,
        employee_id = missed_time.employee_id,
    )

    db.add(to_store)
    db.commit()
    
    return {'message': 'Missed Time stored successfully.'}

@router.put('/{id}')
def update(id: str, missed_time: CreateMissedTime, db: Session = Depends(get_db)): 
    if not db.query(MissedTime).filter(MissedTime.id == id).update({
        'date': missed_time.date,
        'time_log': missed_time.time_log,
        'time_log_type': missed_time.time_log_type,
    }):
        raise HTTPException(404, 'User to update is not found')
    db.commit()
    return {'message': 'Missed Time updated successfully.'}


@router.put('/delete/{id}')
def remove(id: str,  db: Session = Depends(get_db)):
    if not db.query(MissedTime).filter(MissedTime.id == id).update({
        'active_status': "Inactive",
    }):
        raise HTTPException(404, 'Missed Time to delete is not found')
    db.commit()
    return {'message': 'Missed Time removed successfully.'}


@router.put('/update_status/{id}')
def remove(id: str, update: UpdateMissedTime,  db: Session = Depends(get_db)):
    if not db.query(MissedTime).filter(MissedTime.id == id).update({
        'status': update.status
    }):
        raise HTTPException(404, 'Missed Time to update is not found')
    db.commit()
    return {'message': 'Missed Time updated successfully.'}

