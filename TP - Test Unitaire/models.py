from mongoengine import *
# from pydantic import BaseModel


class Perso(Document):
    name = StringField() 
    age = IntField()
    teams = StringField()


# class Test(BaseModel):
#     name : str
#     age : int
#     teams : str
