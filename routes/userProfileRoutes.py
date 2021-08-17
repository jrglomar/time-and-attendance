from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.userProfileSchema import CreateUserProfile
from models.userProfileModel import UserProfile
from database import get_db


router = APIRouter(
    prefix='/userprofiles',
    tags=['userprofiles']
)

@router.get('/')
def all(db: Session = Depends(get_db)):
    users = db.query(UserProfile).all()
    return {'users': users}

@router.get('/{id}')
def read(id: str, db: Session = Depends(get_db)):
    user = db.query(UserProfile).filter(UserProfile.id == id).first()
    if not user:
        raise HTTPException(404, 'User not found')
    return {'user': user}

@router.post('/')
def store(user: CreateUserProfile, db: Session = Depends(get_db)):
    to_store = UserProfile(
        first_name = user.first_name,
        last_name = user.last_name,
        user_id = user.user_id
    )

    db.add(to_store)
    db.commit()
    
    return {'message': 'User profile stored successfully.'}

@router.put('/{id}')
def update(id: str, user: CreateUserProfile, db: Session = Depends(get_db)): 
    if not db.query(UserProfile).filter(UserProfile.id == id).update({
        'name': user.name,
        'age': user.age
    }):
        raise HTTPException(404, 'User to update is not found')
    db.commit()
    return {'message': 'User updated successfully.'}

@router.delete('/{id}')
def remove(id: str, db: Session = Depends(get_db)):
    if not db.query(UserProfile).filter(UserProfile.id == id).delete():
        raise HTTPException(404, 'User to delete is not found')
    db.commit()
    return {'message': 'User removed successfully.'}

