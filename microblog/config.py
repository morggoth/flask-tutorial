from os import environ

class Config:
    SECRET_KEY = environ['SECRET_KEY'] or 'veRry-5ecr31-$tr1n9'