from fastapi import Response, HTTPException, status
from sqlalchemy.orm import Session
from .. import models, schemas


def all(db: Session):

    blogs = db.query(models.Blog).all()
    return blogs


def show(id: int, response: Response, db: Session):

    blog = db.query(models.Blog).filter(models.Blog.id == id).first()

    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog {id} is not in our database.')
        '''response.status_code = status.HTTP_404_NOT_FOUND
        return {'detail': f'Blog {id} is not in our database.'}'''

    return blog


def create(request: schemas.Blog, db: Session):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=request.user_id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)

    return new_blog


def update(id: int, request: schemas.Blog, db: Session):

    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog {id} is not in our database.')

    blog.update(request.__dict__)
    db.commit()

    return (f'New settings for Blog {id} were altered!')


def delete(id: int, db: Session):

    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog {id} is not in our database.')
    
    blog.delete(synchronize_session=False)
    db.commit()

    return (f'Blog {id} deleted!')