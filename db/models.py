from sqlalchemy import Column, Integer, String, ForeignKey, Table
from db.create_db import Base


class Lan(Base):
    __tablename__ = "Lan"
    user_id = Column(Integer, primary_key=True)
    user_language = Column(String)
    def __init__(self,user_id,user_language):
        self.user_id = user_id
        self.user_language = user_language

class Profile(Base):
    __tablename__="Profile"
    user_id = Column(Integer, primary_key=True)
    age = Column(Integer)
    gender = Column(String)
    like = Column(String)
    city = Column(String)
    name = Column(String)
    description = Column(String)
    photo = Column(String)
    def __init__(self,user_id,age,gender,like,city,name,description,photo):
        self.user_id = user_id
        self.age = age
        self.gender = gender
        self.like = like
        self.city = city
        self.name = name
        self.description = description
        self.photo = photo
