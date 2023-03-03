from fastapi import APIRouter,Depends,status,HTTPException
from database import get_db
from sqlalchemy.orm import Session
from typing import List
import models,schemas
from repository import user_repo


router = APIRouter(
        prefix= "/user",
    tags=['User']
)

# create User
@router.post('/',status_code=status.HTTP_201_CREATED,response_model=schemas.ShowUserModel)
def create_user(request:schemas.UserModel,db:Session = Depends(get_db)):
    return user_repo.create_task(request,db)

#Get All User
@router.get('/',response_model=List[schemas.ShowUserModel],status_code=status.HTTP_200_OK)
def all_user(db:Session = Depends(get_db)):
 
        return user_repo.all_user(db)

#Get User by ID
@router.get('/{id}',status_code=200,response_model=schemas.ShowUserModel)
def user_by_id(id,db:Session = Depends(get_db)):
    return user_repo.get_single_user(id,db)

#Delete User
@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT,)
def delete_user(id,db:Session = Depends(get_db)):
    return user_repo.delete_single_user(id,db)

#Update User
@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def updated_users(id,request:schemas.ShowUserModel,db:Session = Depends(get_db)):
    return user_repo.update_single_user(id,request,db)