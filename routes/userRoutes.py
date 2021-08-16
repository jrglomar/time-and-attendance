from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.userSchema import CreateUser
from models.userModel import User
from database import get_db


router = APIRouter(
    prefix='/users',
    tags=['users']
)

@router.get('/')
def all(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return {'users': users}

@router.get('/{id}')
def read(id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(404, 'User not found')
    return {'user': user}

@router.post('/')
def store(user: CreateUser, db: Session = Depends(get_db)):
    to_store = User(
        email = user.email,
        password = user.password,
        user_type_id = user.user_type_id
    )

    db.add(to_store)
    db.commit()
    
    return {'message': 'User stored successfully.'}

@router.put('/{id}')
def update(id: int, user: CreateUser, db: Session = Depends(get_db)): 
    if not db.query(User).filter(User.id == id).update({
        'name': user.name,
        'age': user.age
    }):
        raise HTTPException(404, 'User to update is not found')
    db.commit()
    return {'message': 'User updated successfully.'}

@router.delete('/{id}')
def remove(id: int, db: Session = Depends(get_db)):
    if not db.query(User).filter(User.id == id).delete():
        raise HTTPException(404, 'User to delete is not found')
    db.commit()
    return {'message': 'User removed successfully.'}

