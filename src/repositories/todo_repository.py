from config import db
from sqlalchemy import text
from doi import DOI
from book import Book
from article import Article
from inproceeding import Inproceeding


def get_dois():
    # Fetch books from the Books table
    result = db.session.execute(
        text("SELECT id, doi FROM dois")
    )
    dois = result.fetchall()

    # Map the results to Book objects
    return [DOI(doi[0], doi[1]) for doi in dois]


def get_books():
    # Fetch books from the Books table
    result = db.session.execute(
        text("SELECT * FROM books")
    )
    books = result.fetchall()

    # Map the results to Book objects
    return [Book(book[0], book[1], book[2], book[3], book[4], book[5]) for book in books]


def get_articles():
    # Fetch articles from the articles table
    result = db.session.execute(
        text("SELECT * FROM articles")
    )
    articles = result.fetchall()

    # Map the results to Book objects
    return [Article(article[0], article[1], article[2],\
                     article[3], article[4]) for article in articles]


def get_inproceedings():
    # Fetch inproceedings from the inpreceedings table
    result = db.session.execute(
        text("SELECT * FROM inproceedings")
    )
    inproceedings = result.fetchall()

    # Map the results to Book objects
    return [Inproceeding(inproceeding[0], inproceeding[1], inproceeding[2],\
                          inproceeding[3], inproceeding[4]) for inproceeding in inproceedings]


def create_reference_doi(reference):
    if reference != '':
        # Insert a new doi into dois table
        sql = text(
            """
            INSERT INTO dois (doi)
            VALUES (:doi)
            """
        )
        db.session.execute(sql, {
            "doi": reference

        })
        db.session.commit()


def create_reference_book(reference):
    if reference["author"] != '' and reference["author"] != None:
        sql = text(
            """
            INSERT INTO books (author, title, book_title, publisher, year)
            VALUES (:author, :title, :book_title, :publisher, :year)
            """
        )
        db.session.execute(sql, reference)
        db.session.commit()


def create_reference_article(reference):
    if reference["author"] != '' and reference["author"] != None:
        sql = text(
            """
            INSERT INTO articles (author, title, journal, year)
            VALUES (:author, :title, :journal, :year)
            """
        )
        db.session.execute(sql, reference)
        db.session.commit()

def create_reference_inproceeding(reference):
    if reference["author"] != '' and\
       reference["author"] is not None and reference["book_title"] != None:
        sql = text(
            """
            INSERT INTO inproceedings (author, title, book_title, year)
            VALUES (:author, :title, :book_title, :year)
            """
        )
        db.session.execute(sql, reference)
        db.session.commit()
