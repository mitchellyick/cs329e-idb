'''import json
# using SQLAlchmey, creating a new DB is as easy
# as creating a new object in Python.

# import the following dependencies from SQLAlchmey
# and the empty database we created into our environment
from models import *


def load_json(filename):
    with open(filename) as file:
        jsn = json.load(file)
        file.close()

    return jsn


def create_books():
    book = load_json('books.json')
    Title_details = []
    for oneBook in book:
        tgoogle_id = oneBook.get("google_id","")
        ttitle = oneBook.get("title","")
        tisbn = oneBook.get("isbn","")
        tpublication_date = oneBook.get("publication_date","")
        timage_url = oneBook.get("image_url","")
        tdescription = oneBook.get("description","")
        Title_details.append(Titles(google_id = tgoogle_id, title = ttitle, isbn = tisbn, publication_date = tpublication_date, image_url = timage_url, description = tdescription))
        db.session.add(Title_details)
        db.session.commit()
        publishers = oneBook.get("publishers","")
        publisher_details = []
        for details in publishers:
            pubname = details.get("name","")
            pubwiki_url = details.get("wiki_url","")
            pubdescription = details.get("description","")
            pubowner = details.get("owner","")
            pubimage_url = details.get("image_url","")
            pubweb_link = details.get("web_link","")
            publisher_details.append(Publishers(name = pubname, wiki_url = pubwiki_url, description = pubdescription, owner = pubowner, image_url = pubimage_url, web_link = pubweb_link))
            db.session.add(publisher_details)
            db.session.commit()
        authors = oneBook.get("authors","")
        author_details = []
        for aut_det in authors:
            aname = aut_det.get("name","")
            aborn = aut_det.get("born","")
            adescription = aut_det.get("description","")
            aeducation = aut_det.get("education","")
            anationality = aut_det.get("nationality","")
            awikipedia_url = aut_det.get("wikipedia_url","")
            aimage_url = aut_det.get("image_url","")
            author_details.append(Authors(name = aname, born = aborn, description = adescription, education = aeducation, nationality = anationality, wikipedia_url = awikipedia_url, image_url = aimage_url))
            db.session.add(author_details)
            db.session.commit()


create_books()
'''
import json, logging
# using SQLAlchmey, creating a new DB is as easy
# as creating a new object in Python.

# import the following dependencies from SQLAlchmey
# and the empty database we created into our environment 
from sqlalchemy.orm import sessionmaker
from models import Base, Titles,Authors, Publishers, engine

# bind the engine to the base class. This makes the connection
# between our class definitions and the corresponding tables 
# within our database
Base.metadata.bind = engine

# create session maker object to establish a link 
# of communication between our code execution and 
# the engine we just created
DBSession = sessionmaker(bind=engine)

# in order to create, read, update or delete information 
# on our database, SQLAlchmey executes database operations
# via an interface called a session.
# A session allows us to write down all the commands 
# we want to execute but not send them to the DB 
# until we call "commit"
# create an instance of DBSession
session = DBSession()

def load_json(filename):
    with open(filename) as file:
        jsn = json.load(file)
        file.close()

    return jsn

def create_tables():
    book = load_json('books.json')

    for oneBook in book:
        title = oneBook['title']
        idb = oneBook['google_id']
        try:
            isbn1 = oneBook['isbn']
        except:
            isbn1 = "N/A"
        
        try:
            imurl = oneBook['image_url']
        except:
            imurl = "N/A"

        try:
            pubdate = oneBook['publication_date']
        except:
            pubdate = "N/A"

        try:
            description1 = oneBook['description']
        except:
            description1 = "N/A"
        authorstep1 = oneBook['authors']
        for thing in authorstep1:
            author = thing['name']
        publishersstep1 = oneBook['publishers'] 
        for thinge in publishersstep1:
            pub = thinge['name']
        newBook = Titles(title = title, google_id = idb, isbn = isbn1, publication_date = pubdate, image_url = imurl, description = description1, author = author, publisher = pub, val = 0) 
        session.add(newBook)
        session.commit()
def create_aut():
    counter = 0
    book = load_json('books.json')
    for oneBook in book:
        title = oneBook['title']
        publishersstep1 = oneBook['publishers'] 
        authorstep1 = oneBook['authors']
        for thing in authorstep1:
            author = thing['name']
            try:
                born = thing['born']
            except:
                born = ""
            try: 
                died = thing['died']
            except:
                died = ""
            dob = str(born) + " - " + str(died)
            try:
                education = thing['education']
            except:
                education = "N/A"
            try:
                nat = thing['nationality']
            except:
                nat = "N/A"

            try:
                descAuth = thing['description']
            except:
                descAuth = "N/A"
            try:
                alma = thing['alma_mater']
            except:
                alma = "N/A"
            try:
                wiki = thing['wikipedia_url']
            except:
                wiki = "N/A"
            try:
                a_im_url = thing['image_url']
            except:
                a_im_url = "N/A"
            for thinge in publishersstep1:
                pub = thinge['name']

            newAut =  Authors(born = dob, name = author, education = education, nationality = nat, description = descAuth, alma_mater = alma, wikipedia_url = wiki, image_url = a_im_url, title = title, publisher = pub)
            if session.query(Authors).filter(Authors.name == newAut.name).count() ==0: 
                session.add(newAut)
                session.commit()
                counter +=1


def create_pub():
    counter = 0
    book = load_json('books.json')
    for oneBook in book:
        title = oneBook['title']
        authorstep1 = oneBook['authors']
        publishersstep1 = oneBook['publishers'] 
        for thing in authorstep1:
            author = thing['name']
        for thinge in publishersstep1:
            pub = thinge['name']
            try:
                owner = thing['owner']
            except:
                owner = "N/A"
            try:
                descpub = thing['description']
            except:
                descpub = "N/A"
            try:
                pub_im_url = thing['image_url']
            except:
                pub_im_url = "N/A"
            try:
                website = thing['website']
            except:
                website = "N/A"
            try:
                pub_wiki = thing['wikipedia_url']
            except:
                pub_wiki = "N/A"

            newPub= Publishers(title= title, author= author, name = pub, owner = owner, description = descpub, image_url = pub_im_url, web_link = website, wiki_url = pub_wiki)

        
            if session.query(Publishers).filter(Publishers.name == newPub.name).count() ==0: 
                session.add(newPub)
                session.commit()
        
create_tables()
create_aut()
create_pub()