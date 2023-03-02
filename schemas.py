from typing import List
from pydantic import BaseModel


#task schema
class TaskModel(BaseModel):
    title:str
    body:str
    isFinished:bool
    user_id:int
    assign_to_id:int




#user schema
class UserModel(BaseModel):
    name:str
    email:str
    password:str

#Show user schema
class ShowUserModel(BaseModel):
    name:str
    email:str
    # task:List

    class Config():
        orm_mode = True

#Show task schema
class ShowTaskModel(BaseModel):
    title:str
    body:str
    isFinished:bool
    submitor: object
    creator: object
    class Config():
        orm_mode = True


class Login(BaseModel):
    username:str
    password:str
