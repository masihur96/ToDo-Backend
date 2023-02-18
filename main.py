from fastapi import FastAPI,Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import engine

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



#Task by ID
@app.get('/task/{id}')
def show(id:int):
    return {'data':id}

#Comments of task
@app.get('/task/{id}/comments')
def comments(id):
    return {'data':{'1','2'}}


class TaskModel(BaseModel):
    title:str
    body:str
    finished:bool

def get_db():
    db = SessionLocal()

# create Task
@app.post('/task')
def createtask(request:TaskModel,db:Session = Depends(get_db)):
   
    return {'data':f'Create Task list as {request.title}'}