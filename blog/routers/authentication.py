from fastapi import APIRouter,Depends,status,HTTPException
import schemas,database,models
from sqlalchemy.orm import Session
from hashing import Hash
from mytoken import create_access_token
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
router=APIRouter(
    tags=['authentication']
)
@router.post('/login')
def login(request:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(database.get_db)):
    user=db.query(models.User).filter(models.User.email==request.username).first()
    #we are checking the user
    if not user:
        #if user is not available
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Invalid credentials')
    if not Hash.verify(user.password,request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Incorrect password')
    #generate a JWT token and return
 
    #if everything is fine then we are passing the email to toekn
  
    acess_token= create_access_token(data={"sub":user.email})
    return {"access_token":acess_token,"token_type":"bearer"}
