from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from .. import models, database, hash, tokens

router = APIRouter(
    tags=['Authentication']
)

@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db) ):
    
    user = db.query(models.User).filter(models.User.email == request.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User {id} not in our database.')

    if not hash.verify(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=f'Invalid credentials.')


    access_token = tokens.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}   