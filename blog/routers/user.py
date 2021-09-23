from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import schemas, database
from ..repository import user

router = APIRouter(
    prefix='/user',
    tags=['Users']
    )

@router.get('/{id}', response_model=schemas.ShowUserComplete)
def get_user(id: int, db: Session = Depends(database.get_db)):
    return user.get_user(id, db)


@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(database.get_db)):
    return user.create_user(request, db)