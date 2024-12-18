from fastapi import FastAPI
import models
from database import engine
from routers import blog,user,authentication

app = FastAPI()

models.Base.metadata.create_all(engine)
app.include_router(authentication.router)
app.include_router(blog.router)
#if we are creating any model then we should create it in the database.hence the users table
app.include_router(user.router)





