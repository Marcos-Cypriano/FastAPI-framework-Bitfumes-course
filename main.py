from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'data': {'name': 'Your page'}}

@app.get('/about')
def about():
    return {'data': 'About your page'}