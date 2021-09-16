from pydantic import BaseModel
#from typing import Optional

class Blog(BaseModel):
    title: str
    body: str
    #published: Optional[bool]


class ShowBlog(Blog):
    class Config():
        orm_mode = True


class User(BaseModel):
    name: str
    email: str
    password: str
