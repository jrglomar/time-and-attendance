from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.shiftTypeSchema import CreateShiftType
from models.shiftTypeModel import ShiftType
from database import get_db
from datetime import date


router = APIRouter(
    prefix='/time_and_attendance/api/shifttype',
    tags=['shifttype']
)

@router.get('/')
def all(db: Session = Depends(get_db)):
    shifttype = db.query(ShiftType).filter(ShiftType.active_status == 'Active').all()
    return {'shifttype': shifttype}

@router.get('/{id}')
def read(id: str, db: Session = Depends(get_db)):
    shifttype = db.query(ShiftType).filter(ShiftType.id == id).first()
    if not shifttype:
        raise HTTPException(404, 'Shift type not found')
    return {'shifttype': shifttype}

@router.post('/')
def store(shifttype: CreateShiftType, db: Session = Depends(get_db)):
    to_store = ShiftType(
        title = shifttype.title,
        start_time = shifttype.start_time,
        end_time = shifttype.end_time,
    )

    db.add(to_store)
    db.commit()
    
    return {'message': 'Shift type stored successfully.'}

@router.put('/{id}')
def update(id: str, shifttype: CreateShiftType, db: Session = Depends(get_db)): 
    if not db.query(ShiftType).filter(ShiftType.id == id).update({
        'title': shifttype.title,
        'start_time': shifttype.start_time,
        'end_time': shifttype.end_time,
    }):
        raise HTTPException(404, 'ShiftType to update is not found')
    db.commit()
    return {'message': 'Shift type updated successfully.'}

@router.put('/delete/{id}')
def remove(id: str,  db: Session = Depends(get_db)):
    if not db.query(ShiftType).filter(ShiftType.id == id).update({
        'active_status': "Inactive",
    }):
        raise HTTPException(404, 'Shift type to delete is not found')
    db.commit()
    return {'message': 'Shift type removed successfully.'}

