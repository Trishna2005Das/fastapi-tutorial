from fastapi import HTTPException,status
from sqlalchemy.orm import Session
import models,schemas

def get_all(db:Session):
    blogs=db.query(models.Blog).all()
    return blogs

def create (request:schemas.Blog,db:Session):
    #we do not want db as an query parameter
    new_blog=models.Blog(title=request.title,body=request.body,user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def destroy(id:int,db:Session):
     #blog=db.query(models.Blog).filter(models.Blog.id==id).delete(synchronize_session=False)
    blog=db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'blog with id {id} is not available')
    blog.delete(synchronize_session=False)
    db.commit()
    return 'done'

def update(id:int,request:schemas.Blog,db:Session):
    #db.query(models.Blog).filter(models.Blog.id==id).update({'title':'updated title'})
    blog=db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'blog with id {id} is not available')
    blog.update(request)
    db.commit()
    return 'updated succesfully'
#query.update is a bulk operation that can be used to update multiple rows
# @router.get('/blog',response_model=List[schemas.ShowBlog],tags=['blogs'])
# def all(db:Session=Depends(get_db)):
#     blogs=db.query(models.Blog).all()
#     return blogs

def show(id:int,db:Session):
    blog=db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'blog with id {id} is not available')
        # response.status_code=status.HTTP_404_NOT_FOUND
        # return {'detail':f'blog with id {id} is not available'}
    return blog
