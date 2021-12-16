from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.userTypeSchema import CreateUserType
from models.userTypeModel import UserType
from database import get_db
from datetime import date


router = APIRouter(
    prefix='/time_and_attendance/api/usertype',
    tags=['usertype']
)

@router.get('/')
def all(db: Session = Depends(get_db)):
    usertype = db.query(UserType).filter(UserType.active_status == 'Active').all()
    return {'usertype': usertype}

@router.get('/{id}')
def read(id: str, db: Session = Depends(get_db)):
    usertype = db.query(UserType).filter(UserType.id == id).first()
    if not usertype:
        raise HTTPException(404, 'User Type not found')
    return {'usertype': usertype}

@router.post('/')
def store(usertype: CreateUserType, db: Session = Depends(get_db)):
    to_store = UserType(
        title = usertype.title,
    )

    db.add(to_store)
    db.commit()
    
    return {'message': 'User type stored successfully.'}

@router.put('/{id}')
def update(id: str, usertype: CreateUserType, db: Session = Depends(get_db)): 
    if not db.query(UserType).filter(UserType.id == id).update({
        'title': usertype.title,
    }):
        raise HTTPException(404, 'User to update is not found')
    db.commit()
    return {'message': 'User type updated successfully.'}

@router.put('/delete/{id}')
def remove(id: str,  db: Session = Depends(get_db)):
    if not db.query(UserType).filter(UserType.id == id).update({
        'active_status': "Inactive",
    }):
        raise HTTPException(404, 'Leave type to delete is not found')
    db.commit()
    return {'message': 'User type removed successfully.'}

@router.get('/count/')
def count(db: Session = Depends(get_db)):
    count = db.query(UserType).filter(UserType.active_status == "Active").count()
    return {'count': count}