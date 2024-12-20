from sqlalchemy import text
from config import db, app


# Define table names

BOOKS_TABLE = "books"
DOIS_TABLE = "dois"
ARTICLES_TABLE = "articles"
INPROCEEDINGS_TABLE = "inproceedings"


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

    print("Clearing contents from tables")

    if table_exists(DOIS_TABLE):
        clear_table(DOIS_TABLE)

    if table_exists(BOOKS_TABLE):
        clear_table(BOOKS_TABLE)

    if table_exists(ARTICLES_TABLE):
        clear_table(ARTICLES_TABLE)

    if table_exists(INPROCEEDINGS_TABLE):
        clear_table(INPROCEEDINGS_TABLE)


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

    print("Dropping tables if they exist")

    if table_exists(DOIS_TABLE):
        drop_table(DOIS_TABLE)

    if table_exists(BOOKS_TABLE):
        drop_table(BOOKS_TABLE)

    if table_exists(ARTICLES_TABLE):
        drop_table(ARTICLES_TABLE)

    if table_exists(INPROCEEDINGS_TABLE):
        drop_table(INPROCEEDINGS_TABLE)

    # Create tables

    print(f"Creating table {DOIS_TABLE}")

    sql_str = (
        f"CREATE TABLE {DOIS_TABLE} ("
        "  id SERIAL PRIMARY KEY, "
        "  doi TEXT NOT NULL"
        ")"
    )

    create_table(sql_str)

    print(f"Creating table {BOOKS_TABLE}")

    sql_str = (
        f"CREATE TABLE {BOOKS_TABLE} ("
        "  id SERIAL PRIMARY KEY, "
        "  citation_key TEXT NOT NULL, "
        "  author TEXT NOT NULL, "
        "  title TEXT NOT NULL, "
        "  booktitle TEXT NOT NULL, "
        "  publisher TEXT NOT NULL, "
        "  year INTEGER NOT NULL "
        ")"
    )

    create_table(sql_str)

    print(f"Creating {ARTICLES_TABLE}")

    sql_str = (
        f"CREATE TABLE {ARTICLES_TABLE} ("
        "  id SERIAL PRIMARY KEY, "
        "  citation_key TEXT NOT NULL, "
        "  author TEXT NOT NULL, "
        "  title TEXT NOT NULL, "
        "  journal TEXT NOT NULL, "
        "  year INTEGER NOT NULL "
        ")"
    )

    create_table(sql_str)

    print(f"Creating {INPROCEEDINGS_TABLE}")

    sql_str = (
        f"CREATE TABLE {INPROCEEDINGS_TABLE} ("
        "  id SERIAL PRIMARY KEY, "
        "  citation_key TEXT NOT NULL, "
        "  author TEXT NOT NULL, "
        "  title TEXT NOT NULL, "
        "  booktitle TEXT NOT NULL, "
        "  year INTEGER NOT NULL "
        ")"
    )

    create_table(sql_str)


if __name__ == "__main__":
    with app.app_context():
        reset_db()
        setup_db()
