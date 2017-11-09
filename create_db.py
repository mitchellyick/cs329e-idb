import json
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
