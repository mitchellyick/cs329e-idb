'''
This file defines the models for a book
'''
# for manipulating diff parts of Python's run-time environment
import sys
#import os
# for writing mapper code
from sqlalchemy import Column, ForeignKey, Integer, String

# for configuration and class code
from sqlalchemy.ext.declarative import declarative_base 

# for writing mapper code (create out foreign key relationship)
from sqlalchemy.orm import relationship

# for configuring code at the end of the file
#from sqlalchemy import create_engine


# for creating an instance of the declarative_base class
# (the declarative base class will let SQLAlchemy know 
# that our classes are special SQLAlchemy classes that 
# corresponds to tables in our DB)
#Base = declarative_base()

#class Book(Base):
#	__tablename__ = 'book'
	
#	title = Column(String(80), nullable = False)
#	id = Column(Integer, primary_key = True)

#SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', 'postgresql://postgres:asd123@localhost/bookdb')
#engine = create_engine(SQLALCHEMY_DATABASE_URI)

#Base.metadata.drop_all(engine)
#Base.metadata.create_all(engine)

# try to run this file:
# python create_db.py
# you may receive the following error:
# ImportError: No module named 'psycopg2'
# This indicates that you need to install 'psycopg2' module
# To install the 'psycopg2' module:
# pip install psycopg2
'''
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:asd123@localhost/bookdb'
db = SQLAlchemy(app)


class Titles(db.Model):
    __tablename__ = 'Titles'
    title = db.Column(db.String(80), nullable=False)
    google_id = db.Column(db.String(80), primary_key = True)
    isbn = db.Column(db.String(80))
    publication_date = db.Column(db.String(80))
    image_url = db.Column(db.String(80))
    description = db.Column(db.String(80))


class Authors(db.Model):
    __tablename__ = 'Authors'
    name = db.Column(db.String(80), nullable=False)
    born = db.Column(db.String(50))
    description = db.Column(db.String(100))
    education = db.Column(db.String(100))
    nationality = db.Column(db.String(120))
    wikipedia_url = db.Column(db.String(100), primary_key = True)
    image_url = db.Column(db.String(100))


class Publishers(db.Model):
    __tablename__ = 'Publishers'
    name = db.Column(db.String(80), nullable=False)
    wiki_url = db.Column(db.String(150), primary_key = True)
    description = db.Column(db.String(150))
    owner = db.Column(db.String(100))
    image_url = db.Column(db.String(100))
    web_link = db.Column(db.String(100))


db.drop_all()
db.create_all()
'''
# for manipulating diff parts of Python's run-time environment
import sys
import os
# for writing mapper code
from sqlalchemy import Column, ForeignKey, Integer, String

# for configuration and class code
from sqlalchemy.ext.declarative import declarative_base 

# for writing mapper code (create out foreign key relationship)
from sqlalchemy.orm import relationship, sessionmaker

# for configuring code at the end of the file
from sqlalchemy import create_engine


# for creating an instance of the declarative_base class
# (the declarative base class will let SQLAlchemy know 
# that our classes are special SQLAlchemy classes that 
# corresponds to tables in our DB)
Base = declarative_base()

class Titles(Base):
    __tablename__ = 'Titles'
    title = Column(String(1500), primary_key = True, nullable=False)
    google_id = Column(String(80))
    isbn = Column(String(80))
    publication_date = Column(String(80))
    image_url = Column(String(1000))
    description = Column(String(100000))
    publisher = Column(String(100000))
    author = Column(String(1000))
    val = Column(Integer)

class Authors(Base):
    __tablename__ = 'Authors'
    name = Column(String(1200), primary_key = True, nullable=False)
    born = Column(String(5000))
    description = Column(String(100000))
    education = Column(String(10000))
    nationality = Column(String(120))
    alma_mater = Column(String(200))
    wikipedia_url = Column(String(1000))
    image_url = Column(String(1000))
    publisher = Column(String(100000))
    title = Column(String(10485760))
    val = Column(Integer)

class Publishers(Base):
    __tablename__ = 'Publishers'
    name = Column(String(1200), primary_key = True, nullable=False)
    wiki_url = Column(String(1000))
    description = Column(String(100000))
    owner = Column(String(200))
    image_url = Column(String(1000))
    web_link = Column(String(1000))
    title = Column(String(10485760))
    author = Column(String(10485760))
    val = Column(Integer)

SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', 'postgresql://postgres:asd123@localhost/')
engine = create_engine(SQLALCHEMY_DATABASE_URI)

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# try to run this file:
# python create_db.py
# you may receive the following error:
# ImportError: No module named 'psycopg2'
# This indicates that you need to install 'psycopg2' module
# To install the 'psycopg2' module:
# pip install psycopg2