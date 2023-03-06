from sqlalchemy.orm import Session
import models,schemas
from fastapi import APIRouter,Depends,status,HTTPException



def create_task(request:schemas.TaskModel,db:Session):
        new_task = models.Task(title=request.title,body=request.body,isFinished=request.isFinished,user_id=request.user_id,assign_to_id=request.assign_to_id)
        db.add(new_task)
        db.commit()
        db.refresh(new_task)
        return new_task

def get_all_task(db:Session):
        tasks = db.query(models.Task).all()
        return tasks

def single_task(id:id,db:Session):
        task = db.query(models.Task).filter(models.Task.id==id).first()
        if not task:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Task with the id {id} is not found")
        return task

def delet_single_task(id,db:Session):
        task =db.query(models.Task).filter(models.Task.id==id) 
        if not task.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Task With Id {id} not found")

        task.delete(synchronize_session=False)
        db.commit()
        return {"The Task is Deleted Successfully"}

def update_single_task(id,request:schemas.TaskModel,db:Session):
        task = db.query(models.Task).filter(models.Task.id==id)
        if not task.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Task With Id {id} not found")
        
        task.update({'title':request.title,'body':request.body,'isFinished':request.isFinished})
        db.commit()
        return {"The Task is Updated Successfully"}