from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.shiftTypeSchema import CreateShiftType
from models.shiftTypeModel import ShiftType
from database import get_db


router = APIRouter(
    prefix='/shifttype',
    tags=['shifttype']
)

@router.get('/')
def all(db: Session = Depends(get_db)):
    shifttype = db.query(Employee).all()
    return {'shifttype': shifttype}

@router.get('/{id}')
def read(id: int, db: Session = Depends(get_db)):
    shifttype = db.query(ShiftType).filter(Employee.id == id).first()
    if not shifttype:
        raise HTTPException(404, 'ShiftType not found')
    return {'shifttype': shifttype}

@router.post('/')
def store(shifttype: CreateShiftType, db: Session = Depends(get_db)):
    to_store = ShiftType(
        title = shifttype.title,
    )

    db.add(to_store)
    db.commit()
    
    return {'message': 'ShiftType stored successfully.'}

@router.put('/{id}')
def update(id: int, shifttype: CreateShiftType, db: Session = Depends(get_db)): 
    if not db.query(ShiftType).filter(ShiftType.id == id).update({
        'name': shifttype.name,
        'age': shifttype.age
    }):
        raise HTTPException(404, 'ShiftType to update is not found')
    db.commit()
    return {'message': 'ShiftType updated successfully.'}

@router.delete('/{id}')
def remove(id: int, db: Session = Depends(get_db)):
    if not db.query(ShiftType).filter(ShiftType.id == id).delete():
        raise HTTPException(404, 'User to delete is not found')
    db.commit()
    return {'message': 'ShiftType removed successfully.'}

