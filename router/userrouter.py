from fastapi import APIRouter, HTTPException,status
from pydantic import BaseModel
import bcrypt
router=APIRouter()

class User(BaseModel):
    fullname:str
    email:str
    password:str


fakedb=[]

@router.post("/usercreate",status_code=status.HTTP_200_OK)
async def root(user:User):
    hasedpassword=bcrypt.hashpw(user.password.encode('utf-8'),bcrypt.gensalt())
    newuser={
        "fullname":user.fullname,
        "email":user.email,
        "password":hasedpassword.decode('utf-8')
    }
    fakedb.append(newuser)

    return {"message":"user has been created","user":newuser}

@router.get("/")
async def check(user:User):
    for dbuser in fakedb:
        if dbuser['email'] == user.email:
            if bcrypt.checkpw(user.password.encode('utf-8'), dbuser["password"].encode('utf-8')):
                return {"message": "Authentication successful", "user": dbuser}
            else:
                raise HTTPException(status_code=401, detail="Incorrect password")
    
    raise HTTPException(status_code=404, detail="User not found")

