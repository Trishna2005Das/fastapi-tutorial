from fastapi import Depends,HTTPException,status
from fastapi.security.oauth2 import OAuth2PasswordBearer
import mytoken
oauth2_scheme=OAuth2PasswordBearer(tokenUrl='login')#login route
def get_current_user(token: str=Depends(oauth2_scheme)):
    credentials_exception=HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=f"Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
#to decode the token 
    return mytoken.verify_token(token,credentials_exception)
