from passlib.context import CryptContext
pwd_cxt=CryptContext(schemes=["bcrypt"],deprecated="auto")
class Hash():
    def bycrpt(password: str):
        hashPassword=pwd_cxt.hash(password)
        return hashPassword
        
    def verify(hashed_password,plain_password):
        return pwd_cxt.verify(plain_password,hashed_password)