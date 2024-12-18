from fastapi import APIRouter,Depends,status,HTTPException
from typing import List
import schemas,database,models,oauth2 #routers directory which is inside blog directory 
from sqlalchemy.orm import Session
from repository import blog
get_db=database.get_db
router=APIRouter(
    prefix="/blog",
    tags=['blogs'])

@router.get('/',response_model=List[schemas.ShowBlog])
def all(db:Session=Depends(get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    return blog.get_all(db)

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request:schemas.Blog,db:Session=Depends(get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    return blog.create(request,db)

@router.delete('/blog/{id}',status_code=status.HTTP_204_NO_CONTENT)
def destroy(id,db:Session=Depends(get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
   return blog.destroy(id,db)

@router.put('/blog/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id,request:schemas.Blog,db:Session=Depends(get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    return blog.update(id,request)

@router.get('/blog/{id}',status_code=200,response_model=schemas.ShowBlog)
def show(id,db:Session=Depends(get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    return blog.show(id,db)




