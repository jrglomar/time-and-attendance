from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.userTypeSchema import CreateUserType
from models.userTypeModel import UserType
from database import get_db


router = APIRouter(
    prefix='/usertypes',
    tags=['usertypes']
)

@router.get('/')
def all(db: Session = Depends(get_db)):
    usertypes = db.query(UserType).all()
    return {'usertypes': usertypes}

@router.get('/{id}')
def read(id: int, db: Session = Depends(get_db)):
    usertypes = db.query(UserType).filter(UserType.id == id).first()
    if not usertypes:
        raise HTTPException(404, 'User not found')
    return {'usertypes': usertypes}

@router.post('/')
def store(usertypes: CreateUserType, db: Session = Depends(get_db)):
    to_store = UserType(
        title = usertypes.title,
    )
    
    db.add(to_store)
    db.commit()
    
    return {'message': 'User type stored successfully.'}

@router.put('/{id}')
def update(id: int, usertypes: CreateUserType, db: Session = Depends(get_db)): 
    if not db.query(UserType).filter(UserType.id == id).update({
        'title': usertypes.title,
    }):
        raise HTTPException(404, 'User to update is not found')
    db.commit()
    return {'message': 'User updated successfully.'}

@router.delete('/{id}')
def remove(id: int, db: Session = Depends(get_db)):
    if not db.query(UserType).filter(UserType.id == id).delete():
        raise HTTPException(404, 'User to delete is not found')
    db.commit()
    return {'message': 'User removed successfully.'}

