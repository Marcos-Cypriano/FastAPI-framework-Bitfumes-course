from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get('/')
def index():
    return {'data': {'name': 'Welcome to Marcos-Cypriano FastAPI-framework-Bitfumes-course'}}

@app.get('/about')
def about():
    return {'data': 'About your page'}

@app.get('/blog')
def blog(limit = 10, published: bool = True, sort: Optional[str] = None ):
    #Only get 10 published blogs
    if published:
        return {'data': f'{limit} published blogs from DB'}
    else:
        return {'data': f'{limit} blogs from DB'}

@app.get('/blog/unpublished')
def unpublished():
    #fetch blog unpublished
    return {'data': 'all unpublished blogs'}

@app.get('/blog/{id}')
def show(id: int):
    #fetch blog with id = id
    return {'data': id}


@app.get('/blog/{id}/comments')
def comments(id, limit=10):
    #fetch comments from blog with id = id
    return {'data': { 'comments': id }}
