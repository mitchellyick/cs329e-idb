from flask import Flask
from flask import render_template
from models import Base, Titles, engine, Publishers, Authors
from create_db import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

app = Flask(__name__)
	
@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')
@app.route('/about')
def about():
	return render_template('about.html')
@app.route('/author')
def author():
	authors = session.query(Authors).all()
	return render_template('author.html',authors = authors)
@app.route('/title')
def title():
	books = session.query(Titles).all()
	return render_template('title.html',books = books)		

	#books = session.query(Titles).all()
	#return render_template('title.html', books = books)
@app.route('/publisher')
def publisher():
	pubs = session.query(Publishers).all()
	return render_template('publisher.html',pubs = pubs)		

@app.route('/unit_tests')
def unit_tests():
  output = subprocess.getoutput("python test.py")
  return json.dumps({'output': str(output)})


if __name__ == '__main__':
	app.run()
#host='127.0.0.1',port=8080,debug=True