import os

from app import app
from flask.ext.sqlalchemy import SQLAlchemy

print os.environ.get('SQLALCHEMY_DATABASE_URI')

#app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI', 'postgresql+psycopg2://root:example@192.168.8.111/test')


#olumn = db.Column
# Unicode = db.Unicode
# UnicodeText = db.UnicodeText
# ForeignKey = db.ForeignKey
# DateTime = db.DateTime
# Integer = db.Integer
# Float = db.Float
# PickleType = db.PickleType
# Base = db.Model
# relationship = db.relationship
# synonym = db.synonym


# class PYTest(Base):
#     __tablename__ = 'test'
#
#     id = Column(Integer, primary_key=True)
#     name = Column(Unicode(20))
#
#     def __repr__(self):
#         return "<%s: id=%s, name='%s'>" % (self.__tablename__, self.id, self.name)
