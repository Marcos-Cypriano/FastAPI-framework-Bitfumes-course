from pydantic import BaseModel
from typing import List, Optional


class Blog(BaseModel):
    title: str
    body: str
    user_id: int = 1 
    #published: Optional[bool]
    class Config():
        orm_mode = True

class User(BaseModel):
    name: str
    email: str
    password: str

class ShowUser(BaseModel):
    name: str
    email: str
    
    class Config():
        orm_mode = True

class ShowUserComplete(ShowUser):
    blogs: List[Blog] = []

class UserLogin(BaseModel):
    username: str
    password: str

class ShowBlog(Blog):
    title: str
    body: str
    creator: ShowUser
    class Config():
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None