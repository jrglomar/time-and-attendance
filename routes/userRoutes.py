from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.userSchema import CreateUser
from models.userModel import User
from database import get_db
from jose import jwt
from passlib.context import CryptContext

secret = 'a very shady secret'
pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

def password_verify(plain, hashed):
    return pwd_context.verify(plain, hashed)

def password_hash(password):
    return pwd_context.hash(password)

router = APIRouter(
    prefix='/users',
    tags=['users']
)

@router.get('/')
def all(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return {'users': users}

@router.get('/{id}')
def read(id: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(404, 'User not found')
    return {'user': user}

@router.post('/')
def store(request: CreateUser, db: Session = Depends(get_db)):
    try:
        request.password = password_hash(request.password)
        if request.user_type_id == "" or request.user_type_id == "string":
            user = User(
            email = request.email,
            password = request.password
        )
        else:
            user = User(
                user_type_id = request.user_type_id,
                email = request.email,
                password = request.password
            )
        db.add(user)
        db.commit()
        return {'message': 'Registered Successfully!'}
    except Exception as e:
        print(e)

@router.put('/{id}')
def update(id: str, user: CreateUser, db: Session = Depends(get_db)): 
    if not db.query(User).filter(User.id == id).update({
        'name': user.name,
        'age': user.age
    }):
        raise HTTPException(404, 'User to update is not found')
    db.commit()
    return {'message': 'User updated successfully.'}

@router.delete('/{id}')
def remove(id: str, db: Session = Depends(get_db)):
    if not db.query(User).filter(User.id == id).delete():
        raise HTTPException(404, 'User to delete is not found')
    db.commit()
    return {'message': 'User removed successfully.'}

