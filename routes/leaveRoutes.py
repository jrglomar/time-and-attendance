from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.leaveSchema import CreateLeave, GetLeave
from models.leaveModel import Leave
from database import get_db


router = APIRouter(
    prefix='/time_and_attendance/api/leave',
    tags=['leave']
)

@router.get('/')
def all(db: Session = Depends(get_db)):
    leave = db.query(Leave).all()
    return {'leave': leave}

@router.get('/')
def all(db: Session = Depends(get_db)):
    leave = db.query(Leave).filter(Leave.active_status == 'Active').filter(Leave.employee_id == user.id).all()
    return {'leave': leave}

@router.get('/{id}')
def read(id: str, db: Session = Depends(get_db)):
    leave = db.query(Leave).filter(Leave.id == id).first()
    if not leave:
        raise HTTPException(404, 'Leave not found')
    return {'leave': leave}

@router.post('/')
def store(leave: CreateLeave, db: Session = Depends(get_db)):
    to_store = Leave(
        employee_id = leave.employee_id,
        leave_type_id = leave.leave_type_id,
        leave_sub_type_id = leave.leave_sub_type_id,
        title = leave.title,
        reason = leave.reason,
        start_date = leave.start_date,
        end_date = leave.end_date,
    )

    db.add(to_store)
    db.commit()
    
    return {'message': 'Leave stored successfully.'}

@router.put('/{id}')
def update(id: str, leave: CreateLeave, db: Session = Depends(get_db)): 
    if not db.query(Leave).filter(Leave.id == id).update({
        "employee_id" : leave.employee_id,
        "leave_type_id" : leave.leave_type_id,
        "leave_sub_type_id" : leave.leave_sub_type_id,
        "title" : leave.title,
        "reason" : leave.reason,
        "start_date" : leave.start_date,
        "end_date" : leave.end_date,
        'status': leave.status
    }):
        raise HTTPException(404, 'User to update is not found')
    db.commit()
    return {'message': 'Leave updated successfully.'}

@router.delete('/{id}')
def remove(id: str, db: Session = Depends(get_db)):
    if not db.query(Leave).filter(Leave.id == id).delete():
        raise HTTPException(404, 'User to delete is not found')
    db.commit()
    return {'message': 'Leave removed successfully.'}


@router.post('/getApprovedLeave')
def all(leave_req: GetLeave, db: Session = Depends(get_db)):
    leave = db.query(Leave).filter(Leave.start_date == leave_req.start_date).filter(Leave.status == "Approved").all()
    return {'leave': leave}


@router.get('/userleave/{id}')
def all(id: str, db: Session = Depends(get_db)):
    leave = db.query(Leave).filter(Leave.employee_id == id).filter(Leave.active_status == "Active").all()
    return {'leave': leave}