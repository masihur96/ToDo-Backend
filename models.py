from database import Base
from sqlalchemy import Column,Integer,String,Boolean,ForeignKey
from sqlalchemy.orm import relationship


class Task(Base):
    __tablename__='tasks'
    id=Column(Integer,primary_key=True)
    title= Column(String)
    body=Column(String)
    isFinished=Column(Boolean,default=False)
    user_id= Column(Integer,ForeignKey('users.id'))

    creator = relationship("User",back_populates="task")

    def __repr__(self) :
            return f"<Task {self.title}"

class User(Base):
    __tablename__='users'
    id=Column(Integer,primary_key=True)
    name= Column(String)
    email=Column(String)
    password=Column(String)

    task = relationship("Task",back_populates="creator")

    def __repr__(self) :
            return f"<User {self.name}"
   