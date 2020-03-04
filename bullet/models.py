"""
This is Nether.
Welcome to my world.
address: www.nether.ink
"""
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Text

db = SQLAlchemy()


class BulletScreen(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    author = Column(String(30), default='未名')
    message = Column(Text)
