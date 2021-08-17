from pydantic import BaseModel

class TokenData(BaseModel):
    email: str
    id: str

class AuthForm(BaseModel):
    email: str
    password: str
