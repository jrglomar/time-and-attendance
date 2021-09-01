from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.timeInSchema import CreateTimeIn, CreateCustomTimeIn
from models.timeInModel import TimeIn
from database import get_db


router = APIRouter(
    prefix='/time_and_attendance/api/timein',
    tags=['timein']
)

@router.get('/')
def all(db: Session = Depends(get_db)):
    timein = db.query(TimeIn).filter(TimeIn.active_status == 'Active').all()
    return {'timein': timein}

@router.get('/{id}')
def read(id: str, db: Session = Depends(get_db)):
    timein = db.query(TimeIn).filter(TimeIn.id == id).first()
    if not timein:
        raise HTTPException(404, 'Time in not found')
    return {'timein': timein}

@router.post('/')
def store(timein: CreateTimeIn, db: Session = Depends(get_db)):
    to_store = TimeIn(
        employee_id = timein.employee_id,
        time_log = timein.time_log,
    )

    db.add(to_store)
    db.commit()
    
    return {'message': 'Time in stored successfully.'}

@router.post('/custom_time_in')
def store(timein: CreateCustomTimeIn, db: Session = Depends(get_db)):
    to_store = TimeIn(
        employee_id = timein.employee_id,
        time_log = timein.time_log,
        created_at = timein.created_at,
    )

    db.add(to_store)
    db.commit()
    
    return {'message': 'Time in stored successfully.'}

@router.put('/{id}')
def update(id: str, timein: CreateTimeIn, db: Session = Depends(get_db)): 
    if not db.query(TimeIn).filter(TimeIn.id == id).update({
        'employee_id': timein.employee_id,
        'time_log': timein.time_log,
    }):
        raise HTTPException(404, 'User to update is not found')
    db.commit()
    return {'message': 'Time in updated successfully.'}


@router.put('/delete/{id}')
def remove(id: str,  db: Session = Depends(get_db)):
    if not db.query(TimeIn).filter(TimeIn.id == id).update({
        'active_status': "Inactive",
    }):
        raise HTTPException(404, 'Time in to delete is not found')
    db.commit()
    return {'message': 'Time in removed successfully.'}

