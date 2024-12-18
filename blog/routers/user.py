from fastapi import APIRouter,Depends,status,HTTPException
from typing import List
import schemas,database,models
from sqlalchemy.orm import Session
from hashing import Hash
from repository import user

get_db=database.get_db
router=APIRouter( prefix='/user',
    tags=['users'])

@router.post('/user',response_model=schemas.ShowUser,tags=['users'])
def create_user(request:schemas.User,db:Session=Depends(get_db)):
   return user.create(request,db)
   

#we need to store in the dadtabase so we need the database connection

@router.get('/user/{id}',response_model=schemas.ShowUser,tags=['users'])
def get_user(id:int,db:Session=Depends(get_db)):
   return user.show(id,db)
   
