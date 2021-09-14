from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'data': {'name': 'Welcome to Marcos-Cypriano FastAPI-framework-Bitfumes-course'}}

@app.get('/about')
def about():
    return {'data': 'About your page'}
