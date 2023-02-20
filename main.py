from fastapi import FastAPI,Depends,status,Response,HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import engine
import models,schemas
from typing import List

app=FastAPI()

#Health Check
@app.get('/')
def alltask():
    return {'data':'Your connection is healthy'}




# #Task with Limit & Condition
# @app.get('/task/{limit}')
# def finished(limit:int,published:bool):
#     if published:
#         return {'data':f'{limit} published Task list'}
#     else:
#         return {'data':f'{limit} Unpublished Task list list'}





# #Comments of task
# @app.get('/task/{id}/comments')
# def comments(id):
#     return {'data':{'1','2'}}



#user schema
class UserModel(BaseModel):
    name:str
    email:str
    password:str

def get_db():
    db = Session(bind=engine)
    try:
        yield db
    finally:
        db.close()


#Get All Task
@app.get('/tasks',response_model=List[schemas.ShowTaskModel],status_code=status.HTTP_200_OK)
def all_task(db:Session = Depends(get_db)):
        tasks = db.query(models.Task).all()
        return tasks

#Get Task by ID
@app.get('/task/{id}',status_code=200,response_model=schemas.ShowTaskModel)
def task_by_id(id,response:Response,db:Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id==id).first()
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Task with the id {id} is not found")
    
    return task

#Delete  Task
@app.delete('/tasks/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete_task(id,db:Session = Depends(get_db)):
    task =db.query(models.Task).filter(models.Task.id==id) 
    if not task.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Task With Id {id} not found")
    
    task.delete(synchronize_session=False)
    db.commit()
    return {"The Task is Deleted Successfully"}

#Update Task
@app.put('/tasks/{id}',status_code=status.HTTP_202_ACCEPTED)
def updated_task(id,request:schemas.TaskModel,db:Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id==id)
    if not task.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Task With Id {id} not found")
    
    task.update({'title':request.title,'body':request.body,'isFinished':request.finished})
    db.commit()
    return {"The Task is Updated Successfully"}


# create Task
@app.post('/task',status_code=status.HTTP_201_CREATED)
def create_task(request:schemas.TaskModel,db:Session = Depends(get_db)):
    new_task = models.Task(title=request.title,body=request.body,isFinished=request.finished)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

# create User
@app.post('/user',status_code=status.HTTP_201_CREATED)
def create_user(request:UserModel,db:Session = Depends(get_db)):
    new_user = models.User(name=request.name,email=request.email,password=request.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user