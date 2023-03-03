from fastapi import APIRouter,Depends,status,HTTPException
from database import get_db
from sqlalchemy.orm import Session
from typing import List
import models,schemas,oauth2
from repository import task_repo


router = APIRouter(
    prefix= "/task",
    tags=['Task']
)

@router.get('/',status_code=status.HTTP_200_OK)
def all_task(db:Session = Depends(get_db),current_user:schemas.UserModel=Depends(oauth2.get_current_user)):
        return task_repo.all_task(db)

# create Task
@router.post('/',status_code=status.HTTP_201_CREATED)
def create_task(request:schemas.TaskModel,db:Session = Depends(get_db),current_user:schemas.UserModel=Depends(oauth2.get_current_user)):
    return  task_repo.create_task(request,db)

#Get Task by ID
@router.get('/{id}',status_code=200,response_model=schemas.ShowTaskModel)
def task_by_user(id,db:Session = Depends(get_db),current_user:schemas.UserModel=Depends(oauth2.get_current_user)):
    return task_repo.single_task(id,db)

#Delete  Task
@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete_task(id,db:Session = Depends(get_db),current_user:schemas.UserModel=Depends(oauth2.get_current_user)):
    return task_repo.delet_single_task(id,db)

#Update Task
@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED,)
def updated_task(id,request:schemas.TaskModel,db:Session = Depends(get_db),current_user:schemas.UserModel=Depends(oauth2.get_current_user)):
    return task_repo.update_single_task(id,request,db)


