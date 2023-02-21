from pydantic import BaseModel


#task schema
class TaskModel(BaseModel):
    title:str
    body:str
    isFinished:bool

#Show task schema
class ShowTaskModel(TaskModel):
    class Config():
        orm_mode = True


#user schema
class UserModel(BaseModel):
    name:str
    email:str
    password:str

#Show user schema
class ShowUserModel(BaseModel):
    name:str
    email:str

    class Config():
        orm_mode = True
