from fastapi import FastAPI,Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import engine
import models

app=FastAPI()

#Health Check
@app.get('/')
def alltask():
    return {'data':'Your connection is healthy'}




#Task with Limit & Condition
@app.get('/task/{limit}')
def finished(limit:int,published:bool):
    if published:
        return {'data':f'{limit} published Task list'}
    else:
        return {'data':f'{limit} Unpublished Task list list'}





#Comments of task
@app.get('/task/{id}/comments')
def comments(id):
    return {'data':{'1','2'}}

#task schema
class TaskModel(BaseModel):
    title:str
    body:str
    finished:bool

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
@app.get('/tasks')
def all_task(db:Session = Depends(get_db)):
        tasks = db.query(models.Task).all()
        return tasks

#Task by ID
@app.get('/task/{id}')
def task_by_id(id,db:Session=Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id==id).first()
    return task


# create Task
@app.post('/task')
def create_task(request:TaskModel,db:Session = Depends(get_db)):
    new_task = models.Task(title=request.title,body=request.body,isFinished=request.finished)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

# create User
@app.post('/user')
def create_user(request:UserModel,db:Session = Depends(get_db)):
    new_user = models.User(name=request.name,email=request.email,password=request.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user