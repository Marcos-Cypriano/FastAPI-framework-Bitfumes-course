from typing import List
from fastapi import FastAPI, Depends, status, Response, HTTPException
from . import schemas, models, hash
from .database import engine, SessionLocal
from sqlalchemy.orm import Session
from .database import Base


app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/drop', status_code=status.HTTP_202_ACCEPTED)
def drop_all(db: Session = Depends(get_db)):
    
    Base.metadata.drop_all(bind=engine)

    return 'All tables were dropped successfully!'

@app.post('/blog', status_code=status.HTTP_201_CREATED, tags=['blogs'])
def create(request: schemas.Blog, db: Session = Depends(get_db)):

    new_blog = models.Blog(title=request.title, body=request.body, user_id=request.user_id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)

    return new_blog


@app.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=['blogs'])
def delete(id, db: Session = Depends(get_db)):

    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog {id} is not in our database.')
    
    blog.delete(synchronize_session=False)
    db.commit()

    return f'Blog {id} deleted!'


@app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED, tags=['blogs'])
def update(id, request: schemas.Blog, db: Session = Depends(get_db)):

    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog {id} is not in our database.')

    blog.update(request.__dict__)
    db.commit()

    return f'New settings for Blog {id} were altered!'


@app.get('/blog', response_model=List[schemas.ShowBlog], tags=['blogs'])
def all(db: Session = Depends(get_db)):

    blogs = db.query(models.Blog).all()

    return blogs


@app.get('/blog/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog, tags=['blogs'])
def show(id, response: Response, db: Session = Depends(get_db)):

    blog = db.query(models.Blog).filter(models.Blog.id == id).first()

    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog {id} is not in our database.')
        '''response.status_code = status.HTTP_404_NOT_FOUND
        return {'detail': f'Blog {id} is not in our database.'}'''
    return blog


@app.post('/user', response_model=schemas.ShowUser, tags=['users'])
def create_user(request: schemas.User, db: Session = Depends(get_db)):

    new_user = models.User(name=request.name, email=request.email, password=hash.encrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@app.get('/user/{id}', response_model=schemas.ShowUser, tags=['users'])
def get_user(id,  db: Session = Depends(get_db)):

    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User {id} is not in our database.')
    
    return user