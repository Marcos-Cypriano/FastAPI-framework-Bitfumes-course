from pydantic.main import BaseModel
from sqlalchemy import Column, Integer, String, Boolean
from .database import Base

class Blog(Base):
    __tablename__ = 'Blogs'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    #published = Column(Boolean)


class User(Base):
    __tablename__ = 'Users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)