from sqlalchemy import text
from config import db
from doi import DOI
from book import Book
from article import Article
from inproceeding import Inproceeding

def get_reference(reference_type, id):
    table = ""

    if reference_type == "doi":
        table = "dois"
    elif reference_type == "book":
        table = "books"
    elif reference_type == "article":
        table = "articles"
    elif reference_type == "inproceeding":
        table = "inproceedings"

    sql = f"SELECT * FROM {table} WHERE id={id}"

    result = db.session.execute(
        text(sql)
    )
    
    return result.fetchone()

def get_all_references():
    # Get references from each table
    dois = get_dois()
    books = get_books()
    articles = get_articles()
    inproceedings = get_inproceedings()
    
    # Combine all references into one list
    all_references = {
        'dois': dois,
        'books': books,
        'articles': articles,
        'inproceedings': inproceedings
    }
    
    return all_references

def get_dois():
    # Fetch books from the Books table
    result = db.session.execute(
        text("SELECT * FROM dois")
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
    return [Book(book[0], book[1], book[2], book[3], book[4], book[5], book[6]) for book in books]


def get_articles():
    # Fetch articles from the articles table
    result = db.session.execute(
        text("SELECT * FROM articles")
    )
    articles = result.fetchall()

    # Map the results to Book objects
    return [Article(article[0], article[1], article[2],\
                     article[3], article[4], article[5]) for article in articles]


def get_inproceedings():
    # Fetch inproceedings from the inpreceedings table
    result = db.session.execute(
        text("SELECT * FROM inproceedings")
    )
    inproceedings = result.fetchall()

    # Map the results to Book objects
    return [Inproceeding(inproceeding[0], inproceeding[1], inproceeding[2],\
                          inproceeding[3], inproceeding[4], inproceeding[5]) for inproceeding in inproceedings]


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
    if reference["author"] != '' and reference["author"] is not None:
        sql = text(
            """
            INSERT INTO books (citation_key, author, title, book_title, publisher, year)
            VALUES (:citation_key, :author, :title, :book_title, :publisher, :year)
            """
        )
        db.session.execute(sql, reference)
        db.session.commit()


def create_reference_article(reference):
    if reference["author"] != '' and reference["author"] is not None:
        sql = text(
            """
            INSERT INTO articles (citation_key, author, title, journal, year)
            VALUES (:citation_key, :author, :title, :journal, :year)
            """
        )
        db.session.execute(sql, reference)
        db.session.commit()


def create_reference_inproceeding(reference):
    if reference["author"] != '' and\
       reference["author"] is not None and reference["book_title"] is not None:
        sql = text(
            """
            INSERT INTO inproceedings (citation_key, author, title, book_title, year)
            VALUES (:citation_key, :author, :title, :book_title, :year)
            """
        )
        db.session.execute(sql, reference)
        db.session.commit()


def delete_doi(doi_id):
    sql = text("DELETE FROM dois WHERE id = :id")
    db.session.execute(sql, {"id": doi_id})
    db.session.commit()


def delete_book(book_id):
    sql = text("DELETE FROM books WHERE id = :id")
    db.session.execute(sql, {"id": book_id})
    db.session.commit()


def delete_article(article_id):
    sql = text("DELETE FROM articles WHERE id = :id")
    db.session.execute(sql, {"id": article_id})
    db.session.commit()


def delete_inproceeding(inproceeding_id):
    sql = text("DELETE FROM inproceedings WHERE id = :id")
    db.session.execute(sql, {"id": inproceeding_id})
    db.session.commit()

# Update functions
def update_doi(doi_id, new_doi):
    if new_doi != '':
        sql = text("""
            UPDATE dois 
            SET doi = :doi 
            WHERE id = :id
        """)
        db.session.execute(sql, {
            "id": doi_id,
            "doi": new_doi
        })
        db.session.commit()


def update_book(book_id, book_data):
    if book_data["author"] != '' and book_data["author"] is not None:
        sql = text("""
            UPDATE books 
            SET citation_key = :citation_key,
                author = :author,
                title = :title,
                book_title = :book_title,
                publisher = :publisher,
                year = :year
            WHERE id = :id
        """)
        db.session.execute(sql, {
            "id": book_id,
            "citation_key": book_data["citation_key"],
            "author": book_data["author"],
            "title": book_data["title"],
            "book_title": book_data["book_title"],
            "publisher": book_data["publisher"],
            "year": book_data["year"]
        })
        db.session.commit()


def update_article(article_id, article_data):
    if article_data["author"] != '' and article_data["author"] is not None:
        sql = text("""
            UPDATE articles 
            SET citation_key = :citation_key,
                author = :author,
                title = :title,
                journal = :journal,
                year = :year
            WHERE id = :id
        """)
        db.session.execute(sql, {
            "id": article_id,
            "citation_key": article_data["citation_key"],
            "author": article_data["author"],
            "title": article_data["title"],
            "journal": article_data["journal"],
            "year": article_data["year"]
        })
        db.session.commit()


def update_inproceeding(inproceeding_id, inproceeding_data):
    if (inproceeding_data["author"] != '' and
        inproceeding_data["author"] is not None and
        inproceeding_data["book_title"] is not None):
        sql = text("""
            UPDATE inproceedings 
            SET citation_key = :citation_key,
                author = :author,
                title = :title,
                book_title = :book_title,
                year = :year
            WHERE id = :id
        """)
        db.session.execute(sql, {
            "id": inproceeding_id,
            "citation_key": inproceeding_data["citation_key"],
            "author": inproceeding_data["author"],
            "title": inproceeding_data["title"],
            "book_title": inproceeding_data["book_title"],
            "year": inproceeding_data["year"]
        })
        db.session.commit()
