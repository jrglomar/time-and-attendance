from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.timeOutSchema import CreateTimeOut
from models.timeOutModel import TimeOut
from database import get_db


router = APIRouter(
    prefix='/timeout',
    tags=['timeout']
)

@router.get('/')
def all(db: Session = Depends(get_db)):
    timeout = db.query(TimeOut).all()
    return {'timeout': timeout}

@router.get('/{id}')
def read(id: int, db: Session = Depends(get_db)):
    timeout = db.query(TimeOut).filter(TimeOut.id == id).first()
    if not timeout:
        raise HTTPException(404, 'Time in not found')
    return {'timeout': timeout}

@router.post('/')
def store(timeout: CreateTimeOut, db: Session = Depends(get_db)):
    to_store = TimeOut(
        employee_id = timeout.employee_id,
    )

    db.add(to_store)
    db.commit()
    
    return {'message': 'Time in stored successfully.'}

@router.put('/{id}')
def update(id: int, timeout: CreateTimeOut, db: Session = Depends(get_db)): 
    if not db.query(TimeOut).filter(TimeOut.id == id).update({
        'name': timeout.name,
        'age': timeout.age
    }):
        raise HTTPException(404, 'User to update is not found')
    db.commit()
    return {'message': 'Time in updated successfully.'}

@router.delete('/{id}')
def remove(id: int, db: Session = Depends(get_db)):
    if not db.query(TimeOut).filter(TimeOut.id == id).delete():
        raise HTTPException(404, 'User to delete is not found')
    db.commit()
    return {'message': 'Time in removed successfully.'}

