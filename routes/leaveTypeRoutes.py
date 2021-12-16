from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.leaveTypeSchema import CreateLeaveType
from models.leaveTypeModel import LeaveType
from database import get_db
from datetime import date


router = APIRouter(
    prefix='/time_and_attendance/api/leavetype',
    tags=['leavetype']
)

@router.get('/')
def all(db: Session = Depends(get_db)):
    leavetype = db.query(LeaveType).filter(LeaveType.active_status == 'Active').all()
    return {'leavetype': leavetype}

@router.get('/{id}')
def read(id: str, db: Session = Depends(get_db)):
    leavetype = db.query(LeaveType).filter(LeaveType.id == id).first()
    if not leavetype:
        raise HTTPException(404, 'LeaveType not found')
    return {'leavetype': leavetype}

@router.post('/')
def store(leavetype: CreateLeaveType, db: Session = Depends(get_db)):
    to_store = LeaveType(
        title = leavetype.title,
    )

    db.add(to_store)
    db.commit()
    
    return {'message': 'LeaveType stored successfully.'}

@router.put('/{id}')
def update(id: str, leavetype: CreateLeaveType, db: Session = Depends(get_db)): 
    if not db.query(LeaveType).filter(LeaveType.id == id).update({
        'title': leavetype.title,
    }):
        raise HTTPException(404, 'Leave Type to update is not found')
    db.commit()
    return {'message': 'LeaveType updated successfully.'}

@router.put('/delete/{id}')
def remove(id: str,  db: Session = Depends(get_db)):
    if not db.query(LeaveType).filter(LeaveType.id == id).update({
        'active_status': "Inactive",
    }):
        raise HTTPException(404, 'Leave type to delete is not found')
    db.commit()
    return {'message': 'Leave type removed successfully.'}

@router.get('/count/')
def count(db: Session = Depends(get_db)):
    count = db.query(LeaveType).filter(LeaveType.active_status == "Active").count()
    return {'count': count}