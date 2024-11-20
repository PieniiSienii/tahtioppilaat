from config import db
from sqlalchemy import text
from doi import DOI
from book import Book

def get_books():
    # Fetch books from the Books table
    result = db.session.execute(
        text("SELECT id, doi FROM DOIs")
    )
    dois = result.fetchall()
    
    # Map the results to Book objects
    return [DOI(doi[0], doi[1]) for doi in dois] 


def create_reference(doi):
    # Insert a new book into the Books table
    sql = text(
        """
        INSERT INTO dois (doi)
        VALUES (:doi)
        """
    )
    db.session.execute(sql, {
        "doi": doi

    })
    db.session.commit()
