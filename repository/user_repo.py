from sqlalchemy.orm import Session
import models,schemas
from fastapi import Depends,status,HTTPException
from hashing import Hash


def create_task(request:schemas.UserModel,db:Session):
    new_user = models.User(name=request.name,email=request.email,password=Hash.bncrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def all_user(db:Session):
        users = db.query(models.User).all()
        return users

def get_single_user(id,db:Session):
        user = db.query(models.User).filter(models.User.id==id).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"User with the id {id} is not found")
        
        return user

def delete_single_user(id,db:Session):
        user =db.query(models.User).filter(models.User.id==id) 
        if not user.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"User With Id {id} not found")
        
        user.delete(synchronize_session=False)
        db.commit()
        return {"The User is Deleted Successfully"}

def update_single_user(id,request:schemas.ShowUserModel,db:Session):
        user = db.query(models.User).filter(models.User.id==id)
        if not user.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"User With Id {id} not found")
        
        user.update({'name':request.name,'email':request.email})
        db.commit()
        return {"The User is Updated Successfully"}