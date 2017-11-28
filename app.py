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
	books = session.query(Titles).all()
	pubs = session.query(Publishers).all()
	return render_template('author.html',authors = authors, books = books, pubs = pubs)
@app.route('/title')
def title():
	#books = session.query(Titles).all()
	#return render_template('title.html', books = books)
	authors = session.query(Authors).all()
	books = session.query(Titles).all()
	pubs = session.query(Publishers).all()
	return render_template('title.html', authors = authors, books = books, pubs = pubs)	
@app.route('/publisher')
def publisher():
	authors = session.query(Authors).all()
	books = session.query(Titles).all()
	pubs = session.query(Publishers).all()
	return render_template('publisher.html', authors = authors, books = books, pubs = pubs)

@app.route('/publisher/<publisher_name>')
def publisher_page(publisher_name):
	info = session.query(Publishers).all()
	authors = session.query(Authors).all()
	books = session.query(Titles).all()
	for i in info:
		if i.name ==publisher_name:
			owner = i.owner
			publisher_description = i.description
			website = i.web_link
			publisher_image_url = i.image_url

	lia = []
	for i in authors:
		if i.publisher == publisher_name:
			if i.name not in lia:
				lia.append(i.name)
	lib = []
	for i in books:
		if i.publisher == publisher_name:
			if i.title not in lib:
				lib.append(i.title)
	
	return render_template('i_publisher.html', info=info, publisher_name=publisher_name, owner=owner, publisher_description = publisher_description, \
	website=website, publisher_image_url=publisher_image_url, lia=lia, lib=lib)
@app.route('/title/<book_title>')
def title_page(book_title):
	info = session.query(Publishers).all()
	authors = session.query(Authors).all()
	books = session.query(Titles).all()
	for i in books:
		if i.title ==book_title:
			author = i.author
			google_id = i.google_id
			isbn = i.isbn
			title_image_url = i.image_url
			pub_date = i.publication_date
			book_descrip = i.description
			pub = i.publisher

	
	return render_template('i_title.html', info=info, book_title=book_title, author=author, google_id = google_id, \
	isbn=isbn, title_image_url=title_image_url, pub_date=pub_date, book_descrip=book_descrip, pub = pub)

@app.route('/author/<author_name>')
def author_page(author_name):
	info = session.query(Publishers).all()
	authors = session.query(Authors).all()
	books = session.query(Titles).all()
	for i in authors:
		if i.name ==author_name:
			dob = i.born 
			author_description = i.description
			education = i.education
			nationality = i.nationality
			alma_mater = i.alma_mater
			wiki_url = i.wikipedia_url
			image_url = i.image_url
			
	lip = []
	for i in info:
		if i.author == author_name:
			if i.name not in lip:
				lip.append(i.name)
	lib = []
	for i in books:
		if i.author == author_name:
			if i.title not in lib:
				lib.append(i.title)
	return render_template('i_authors.html', info=info, author_name=author_name, dob=dob, author_description = author_description, \
	education=education, nationality=nationality, alma_mater=alma_mater, image_url = image_url, wiki_url=wiki_url, publisher = lip, title = lib)

@app.route('/unit_tests')
def unit_tests():
  output = subprocess.getoutput("python test.py")
  return json.dumps({'output': str(output)})


if __name__ == '__main__':
	app.run()
#host='127.0.0.1',port=8080,debug=True