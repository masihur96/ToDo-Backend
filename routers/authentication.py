from fastapi import APIRouter,Depends,status,HTTPException
from fastapi.security import OAuth2PasswordRequestForm
import models,schemas,database,jwt_token
from sqlalchemy.orm import Session
from hashing import Hash

router = APIRouter(
        prefix= "/login",
    tags=['Authentication']
)


@router.post('')
def login(request:OAuth2PasswordRequestForm=Depends(),db:Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
          raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Invalid Creadentials")
    if not Hash.verify(user.password,request.password):
          raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Incorrect Password")
    
  
    access_token = jwt_token.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
