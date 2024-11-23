from config import db
from sqlalchemy import text
from doi import DOI
from book import Book

def get_dois():
    # Fetch books from the Books table
    result = db.session.execute(
        text("SELECT id, doi FROM DOIs")
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

def create_reference(reference):
    # Insert a new book into the Books table
    if reference == str:
        sql = text(
            """
            INSERT INTO dois (reference)
            VALUES (:reference)
            """
        )
        db.session.execute(sql, {
            "reference": reference

        })
        db.session.commit()

    if reference == dict:
        id = reference["id"]
        author = reference["author"]
        title = reference["title"]
        book_title = reference["book_title"]
        publisher = reference["publisher"]
        year = reference["year"]
        reference = [author, title, book_title, publisher, year]
        sql = text(
            """
            INSERT INTO books (author, title, book_title, publisher, year)
            VALUES (:author, :title, :book_title, :publisher, :year)
            """
        )
        db.session.execute(sql, {
        "author": reference["author"],
        "title": reference["title"],
        "book_title": reference["book_title"],
        "publisher": reference["publisher"],
        "year": reference["year"]
        })
        db.session.commit()


