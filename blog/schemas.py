
from pydantic import BaseModel
from typing import List,Optional

#there are two types of model sqlalchemy and pydantic
#the pydantic model is used to create the schema for the api
class BlogBase(BaseModel):
    title: str
    body: str

class Blog(BlogBase):
    class Config():
        form_mode = True

# class ShowBlog (Blog):
#     class Config():
#         orm_mode = True
# #since it is an extension of class Blog hence the paramters are inherited

class ShowUser(BaseModel):
    name : str
    email : str
    blogs: List[BlogBase]
    class Config():
        orm_mode = True

class ShowBlog (BaseModel):
    title: str
    body: str
    creator: Optional[ShowUser]
    class Config():
        orm_mode = True
    

class User(BaseModel):
    name: str
    email: str
    password: str

class Login(BaseModel):
    username: str
    password: str
    #JWT needs username as the indentifier of the user but it is the same as email

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str]=None