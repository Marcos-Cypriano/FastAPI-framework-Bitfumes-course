from fastapi import FastAPI, Depends, status
from sqlalchemy.orm import Session
from . import models
from .database import engine, get_db, Base
from .routers import blog, user, login

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(login.router)
app.include_router(blog.router)
app.include_router(user.router)


@app.post('/drop', status_code=status.HTTP_202_ACCEPTED)
def drop_all(db: Session = Depends(get_db)):
    
    Base.metadata.drop_all(bind=engine)

    return 'All tables were dropped successfully!'