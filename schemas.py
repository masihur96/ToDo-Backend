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