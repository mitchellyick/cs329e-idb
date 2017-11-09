from create_db import create_books, load_json
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
from flask_testing import TestCase

class MyTest(TestCase):

	def test_create(self):
		load_json(books.json)
		create_books()

		assert Title_details in db.session
		