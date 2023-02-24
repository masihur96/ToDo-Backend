from typing import List
from pydantic import BaseModel


#task schema
class TaskModel(BaseModel):
    title:str
    body:str
    isFinished:bool




#user schema
class UserModel(BaseModel):
    name:str
    email:str
    password:str

#Show user schema
class ShowUserModel(BaseModel):
    name:str
    email:str
    task:List

    class Config():
        orm_mode = True

#Show task schema
class ShowTaskModel(BaseModel):
    title:str
    body:str
    isFinished:bool
    creator:ShowUserModel
    class Config():
        orm_mode = True