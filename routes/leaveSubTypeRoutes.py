from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.leaveSubTypeSchema import CreateLeaveSubType
from models.leaveSubTypeModel import LeaveSubType
from database import get_db
from datetime import date


router = APIRouter(
    prefix='/time_and_attendance/api/leavesubtype',
    tags=['leavesubtype']
)

@router.get('/')
def all(db: Session = Depends(get_db)):
    leavesubtype = db.query(LeaveSubType).filter(LeaveSubType.active_status == 'Active').all()
    return {'leavesubtype': leavesubtype}

@router.get('/leave_type/{id}')
def all(id: str, db: Session = Depends(get_db)):
    leavesubtype = db.query(LeaveSubType).filter(LeaveSubType.leave_type_id == id).filter(LeaveSubType.active_status == 'Active').all()
    return {'leavesubtype': leavesubtype}

@router.get('/{id}')
def read(id: str, db: Session = Depends(get_db)):
    leavesubtype = db.query(LeaveSubType).filter(LeaveSubType.id == id).first()
    if not leavesubtype:
        raise HTTPException(404, 'Leave Sub Type not found')
    return {'leavesubtype': leavesubtype}

@router.post('/')
def store(leavesubtype: CreateLeaveSubType, db: Session = Depends(get_db)):
    to_store = LeaveSubType(
        title = leavesubtype.title,
        leave_type_id = leavesubtype.leave_type_id,
        number_of_days = leavesubtype.number_of_days,
    )

    db.add(to_store)
    db.commit()
    
    return {'message': 'Leave Sub Type stored successfully.'}

@router.put('/{id}')
def update(id: str, leavesubtype: CreateLeaveSubType, db: Session = Depends(get_db)): 
    if not db.query(LeaveSubType).filter(LeaveSubType.id == id).update({
        'title': leavesubtype.title,
        'leave_type_id': leavesubtype.leave_type_id,
        'number_of_days': leavesubtype.number_of_days,
        
    }):
        raise HTTPException(404, 'Leave Sub Type to update is not found')
    db.commit()
    return {'message': 'Leave Sub Type updated successfully.'}

@router.put('/delete/{id}')
def remove(id: str,  db: Session = Depends(get_db)):
    if not db.query(LeaveSubType).filter(LeaveSubType.id == id).update({
        'active_status': "Inactive",
    }):
        raise HTTPException(404, 'Leave Sub Type to delete is not found')
    db.commit()
    return {'message': 'Leave Sub Type removed successfully.'}

@router.get('/count/')
def count(db: Session = Depends(get_db)):
    count = db.query(LeaveSubType).filter(LeaveSubType.active_status == "Active").count()
    return {'count': count}