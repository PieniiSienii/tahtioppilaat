from config import db, app
from sqlalchemy import text

# Define table names
books_table = "Books"
dois_table = "DOIs"

def table_exists(name):
    """Check if a table exists in the database."""
    sql_table_existence = text(
        "SELECT EXISTS ("
        "  SELECT 1"
        "  FROM information_schema.tables"
        f" WHERE table_name = '{name}'"
        ")"
    )

    print(f"Checking if table {name} exists")
    result = db.session.execute(sql_table_existence)
    return result.fetchall()[0][0]

def reset_db():
    """Clear contents from existing tables (if any) before dropping them."""
    print(f"Clearing contents from tables {books_table} and {dois_table}")

    # Clear contents from DOIs table first to avoid foreign key conflicts
    if table_exists(dois_table):
        sql = text(f"DELETE FROM {dois_table}")
        db.session.execute(sql)

    if table_exists(books_table):
        sql = text(f"DELETE FROM {books_table}")
        db.session.execute(sql)

    db.session.commit()

def setup_db():
    """Drop existing tables and recreate them."""
    # Drop DOIs table if it exists
    if table_exists(dois_table):
        print(f"Table {dois_table} exists, dropping")
        sql = text(f"DROP TABLE {dois_table}")
        db.session.execute(sql)
        db.session.commit()

    # Drop Books table if it exists
    if table_exists(books_table):
        print(f"Table {books_table} exists, dropping")
        sql = text(f"DROP TABLE {books_table}")
        db.session.execute(sql)
        db.session.commit()

    # Create DOIs table
    print(f"Creating table {dois_table}")
    sql = text(
        f"CREATE TABLE {dois_table} ("
        "  id SERIAL PRIMARY KEY, "
        "  doi TEXT NOT NULL UNIQUE"
        ")"
    )
    db.session.execute(sql)

    db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        setup_db()
