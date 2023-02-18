from database import Base
from sqlalchemy import Column,Integer,String,Boolean,Text

class Task(Base):
    __tablename__='task'
    id=Column(Integer,primary_key=True)
    title= Column(String(25),unique=True)
    body=Column(String(80),unique=True)
    isFinished=Column(Boolean)

    def __repr__(self) :
            return f"<Task {self.title}"

class User(Base):
    __tablename__='user'
    id=Column(Integer,primary_key=True)
    name= Column(String(25),unique=True)
    password=Column(String(20),unique=True)
    isFinished=Column(Boolean,default=False)

    def __repr__(self) :
            return f"<User {self.name}"
   