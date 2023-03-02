from fastapi import APIRouter,Depends,status,HTTPException
import models,schemas,database
from sqlalchemy.orm import Session

router = APIRouter(
        prefix= "/login",
    tags=['Authentication']
)


@router.post('')
def login(request:schemas.Login,db:Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
          raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Invalid Creadentials")
    return user
