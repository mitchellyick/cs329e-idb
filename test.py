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
from models import Base, Titles, engine
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
        s = create_books()
        r = s.(Titles).filter_by(google_id = 'wrOQLV6xB-wC').one()
        self.assertEqual(str(r.google_id), 'wrOQLV6xB-wC')

if __name__ == '__main__':
	unittest.main()