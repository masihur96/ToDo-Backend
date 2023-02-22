from fastapi import FastAPI,Depends,status,Response,HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import engine
import models,schemas
from hashing import Hash
from typing import List


app=FastAPI()

#Health Check
@app.get('/')
def Health():
    return {'data':'Your connection is healthy'}

def get_db():
    db = Session(bind=engine)
    try:
        yield db
    finally:
        db.close()


#Get All Task
@app.get('/tasks',response_model=List[schemas.ShowTaskModel],status_code=status.HTTP_200_OK,tags=['task'])
def all_task(db:Session = Depends(get_db)):
        tasks = db.query(models.Task).all()
        return tasks

#Get Task by ID
@app.get('/task/{id}',status_code=200,response_model=schemas.ShowTaskModel,tags=['task'])
def task_by_id(id,response:Response,db:Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id==id).first()
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Task with the id {id} is not found")
    
    return task

#Delete  Task
@app.delete('/tasks/{id}',status_code=status.HTTP_204_NO_CONTENT,tags=['task'])
def delete_task(id,db:Session = Depends(get_db)):
    task =db.query(models.Task).filter(models.Task.id==id) 
    if not task.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Task With Id {id} not found")
    
    task.delete(synchronize_session=False)
    db.commit()
    return {"The Task is Deleted Successfully"}

#Update Task
@app.put('/tasks/{id}',status_code=status.HTTP_202_ACCEPTED,tags=['task'])
def updated_task(id,request:schemas.TaskModel,db:Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id==id)
    if not task.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Task With Id {id} not found")
    
    task.update({'title':request.title,'body':request.body,'isFinished':request.isFinished})
    db.commit()
    return {"The Task is Updated Successfully"}


# create Task
@app.post('/task',status_code=status.HTTP_201_CREATED,tags=['task'])
def create_task(request:schemas.TaskModel,db:Session = Depends(get_db)):
    new_task = models.Task(title=request.title,body=request.body,isFinished=request.isFinished,user_id=1)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task




# create User
@app.post('/user',status_code=status.HTTP_201_CREATED,response_model=schemas.ShowUserModel,tags=['user'])
def create_user(request:schemas.UserModel,db:Session = Depends(get_db)):
    new_user = models.User(name=request.name,email=request.email,password=Hash.bncrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

#Get All User
@app.get('/users',response_model=List[schemas.ShowUserModel],status_code=status.HTTP_200_OK,tags=['user'])
def all_user(db:Session = Depends(get_db)):
        users = db.query(models.User).all()
        return users

#Get User by ID
@app.get('/user/{id}',status_code=200,response_model=schemas.ShowUserModel,tags=['user'])
def user_by_id(id,response:Response,db:Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id==id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"User with the id {id} is not found")
    
    return user

#Delete User
@app.delete('/users/{id}',status_code=status.HTTP_204_NO_CONTENT,tags=['user'])
def delete_user(id,db:Session = Depends(get_db)):
    user =db.query(models.User).filter(models.User.id==id) 
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"User With Id {id} not found")
    
    user.delete(synchronize_session=False)
    db.commit()
    return {"The User is Deleted Successfully"}

#Update User
@app.put('/users/{id}',status_code=status.HTTP_202_ACCEPTED,tags=['user'])
def updated_users(id,request:schemas.ShowUserModel,db:Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id==id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"User With Id {id} not found")
    
    user.update({'name':request.name,'email':request.email})
    db.commit()
    return {"The User is Updated Successfully"}