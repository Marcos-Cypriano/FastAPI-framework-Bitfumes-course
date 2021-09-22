from re import L
from pydantic import BaseModel
from typing import List
#from typing import Optional

class Blog(BaseModel):
    title: str
    body: str
    user_id: int
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
    blogs: List[Blog] = []
    class Config():
        orm_mode = True

class ShowBlog(Blog):
    title: str
    body: str
    creator: ShowUser
    class Config():
        orm_mode = True