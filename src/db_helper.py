from config import db, app
from sqlalchemy import text

# Define table names

books_table = "books"
dois_table = "dois"
articles_table = "articles"
inproceedings_table = "inproceedings"


# Check if table exists in the database

def table_exists(name):
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


# Clear contents from tables first to avoid foreign key conflicts

def reset_db():
    def clear_table(table_name):
        sql = text(f"DELETE FROM {table_name}")
        db.session.execute(sql)
        db.session.commit()

    print(f"Clearing contents from tables")

    if table_exists(dois_table):
        clear_table(dois_table)

    if table_exists(books_table):
        clear_table(books_table)

    if table_exists(articles_table):
        clear_table(articles_table)

    if table_exists(inproceedings_table):
        clear_table(inproceedings_table)


# Drop existing tables and recreate them

def setup_db():
    def drop_table(table_name):
        print(f"Table {table_name} exists, dropping")
        sql = text(f"DROP TABLE {table_name}")
        db.session.execute(sql)
        db.session.commit()

    def create_table(sql_str):
        sql = text(sql_str)
        db.session.execute(sql)
        db.session.commit()

    print(f"Dropping tables if they exist")

    if table_exists(dois_table):
        drop_table(dois_table)

    if table_exists(books_table):
        drop_table(books_table)

    if table_exists(articles_table):
        drop_table(articles_table)

    if table_exists(inproceedings_table):
        drop_table(inproceedings_table)

    # Create tables

    print(f"Creating table {dois_table}")

    sql_str = (
        f"CREATE TABLE {dois_table} ("
        "  id SERIAL PRIMARY KEY, "
        "  doi TEXT NOT NULL"
        ")"
    )

    create_table(sql_str)

    print(f"Creating table {books_table}")

    sql_str = (
        f"CREATE TABLE {books_table} ("
        "  id SERIAL PRIMARY KEY, "
        "  author TEXT NOT NULL, "
        "  title TEXT NOT NULL, "
        "  book_title TEXT NOT NULL, "
        "  publisher TEXT NOT NULL, "
        "  year INTEGER NOT NULL "
        ")"
    )

    create_table(sql_str)

    print(f"Creating {articles_table}")

    sql_str = (
        f"CREATE TABLE {articles_table} ("
        "  id SERIAL PRIMARY KEY, "
        "  author TEXT NOT NULL, "
        "  title TEXT NOT NULL, "
        "  journal TEXT NOT NULL, "
        "  year INTEGER NOT NULL "
        ")"
    )

    create_table(sql_str)

    print(f"Creating {inproceedings_table}")

    sql_str = (
        f"CREATE TABLE {inproceedings_table} ("
        "  id SERIAL PRIMARY KEY, "
        "  author TEXT NOT NULL, "
        "  title TEXT NOT NULL, "
        "  book_title TEXT NOT NULL, "
        "  year INTEGER NOT NULL "
        ")"
    )

    create_table(sql_str)


if __name__ == "__main__":
    with app.app_context():
        reset_db()
        setup_db()
