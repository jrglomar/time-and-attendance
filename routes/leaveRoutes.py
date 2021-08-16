from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.leaveSchema import CreateLeave
from models.leaveModel import Leave
from database import get_db


router = APIRouter(
    prefix='/leave',
    tags=['leave']
)

@router.get('/')
def all(db: Session = Depends(get_db)):
    leave = db.query(Leave).all()
    return {'leave': leave}

@router.get('/{id}')
def read(id: int, db: Session = Depends(get_db)):
    leave = db.query(Leave).filter(Leave.id == id).first()
    if not leave:
        raise HTTPException(404, 'Leave not found')
    return {'leave': leave}

@router.post('/')
def store(leave: CreateLeave, db: Session = Depends(get_db)):
    to_store = Leave(
        employee_id = leave.employee_id,
        leave_type_id = leave.leave_type_id,
        title = leave.title,
        reason = leave.reason,
        start_date = leave.start_date,
        end_date = leave.end_date,
    )

    db.add(to_store)
    db.commit()
    
    return {'message': 'Leave stored successfully.'}

@router.put('/{id}')
def update(id: int, leave: CreateLeave, db: Session = Depends(get_db)): 
    if not db.query(Leave).filter(Leave.id == id).update({
        'name': leave.name,
        'age': leave.age
    }):
        raise HTTPException(404, 'User to update is not found')
    db.commit()
    return {'message': 'Leave updated successfully.'}

@router.delete('/{id}')
def remove(id: int, db: Session = Depends(get_db)):
    if not db.query(Leave).filter(Leave.id == id).delete():
        raise HTTPException(404, 'User to delete is not found')
    db.commit()
    return {'message': 'Leave removed successfully.'}
