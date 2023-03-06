from typing import List,Union,Optional
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
    id:int
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


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None
