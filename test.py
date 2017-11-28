'''from create_db import *
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
#from flask_testing import TestCase

def test_create(self):
	create_books()
	r = session.query()
'''
import os
import unittest
from models import Base, Titles, engine, Publishers, Authors
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from create_db import *
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

class DBTestCases(unittest.TestCase):
    def test_source_insert_1(self):
        s = Titles(google_id='20', title = 'C++')
        session.add(s)
        session.commit()
        r = session.query(Titles).filter_by(google_id = '20').one()
        self.assertEqual(str(r.google_id), '20')

        session.query(Titles).filter_by(google_id = '20').delete()
        session.commit()

    def test_db_there_1(self):
        #s = create_books()
        r = session.query(Titles).filter_by(google_id = 'wrOQLV6xB-wC').one()
        self.assertEqual(str(r.google_id), 'wrOQLV6xB-wC')
    def test_db_there_2(self):
        #s = create_books()
        r = session.query(Titles).filter_by(google_id = 'kPpeTrfXpKsC').first()
        self.assertEqual(str(r.google_id), 'kPpeTrfXpKsC')
    def test_db_there_3(self):
        #s = create_books()
        r = session.query(Titles).filter_by(isbn = '1101486406').first()
        self.assertEqual(str(r.isbn), '1101486406')
    def test_db_there_4(self):
        #s = create_books()
        r = session.query(Titles).filter_by(title = 'Royal Assassin').first()
        self.assertEqual(str(r.title), 'Royal Assassin')
    def test_db_there_5(self):
        #s = create_books()
        r = session.query(Authors).filter_by(name = 'Terry Goodkind').first()
        self.assertEqual(str(r.name), 'Terry Goodkind')
    def test_db_there_6(self):
        #s = create_books()
        r = session.query(Authors).filter_by(born = '1963-07-19').first()
        self.assertEqual(str(r.born), '1963-07-19') 
    def test_db_there_7(self):
        #s = create_books()
        r = session.query(Authors).filter_by(education = 'Dana Hall School, 1928').first()
        self.assertEqual(str(r.education), 'Dana Hall School, 1928') 
    def test_db_there_8(self):
        #s = create_books()
        r = session.query(Authors).filter_by(alma_mater = 'Princeton University').first()
        self.assertEqual(str(r.alma_mater), 'Princeton University')                    
if __name__ == '__main__':
	unittest.main()