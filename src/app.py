from flask import redirect, render_template, request, jsonify, flash
from db_helper import reset_db
from repositories.todo_repository import get_books, create_reference_doi, create_reference_book, create_reference_article, create_reference_inproceeding, get_dois, get_articles, get_inproceedings
from config import app, test_env
from util import validate_todo

@app.route("/", methods=["POST", "GET"])
def index():
    # Fetch dois (or references) from the database
    dois = [i.doi for i in get_dois()]
    # return render_template("index.html", dois=dois)  # Pass 'dois' instead of 'doi'
    # Fetch books (or references) from the database
    books = get_books()
    articles = get_articles()
    inproceedings = get_inproceedings()
    return render_template("index.html", books=books, dois=dois, articles=articles, inproceedings=inproceedings)  # Pass 'dois' instead of 'doi'

@app.route("/create_reference", methods=["POST"])
def reference_creation():
    # Handle doi case
    doi_reference = request.form.get("doi")
    
    # Handle manual entry case
    book_reference = {
        "author": request.form.get("book_author"),
        "title": request.form.get("book_title"),
        "book_title": request.form.get("book_book_title"),
        "publisher": request.form.get("book_publisher"),
        "year": request.form.get("book_year")
    }
    article_reference = {
        "author": request.form.get("article_author"),
        "title": request.form.get("article_title"),
        "journal": request.form.get("article_journal"),
        "year": request.form.get("article_year")
    }
    inproceeding_reference = {
        "author": request.form.get("inproceeding_author"),
        "title": request.form.get("inproceeding_title"),
        "book_title": request.form.get("inproceeding_book_title"),
        "year": request.form.get("inproceeding_year"),
    }
    # Save reference to database
    create_reference_doi(doi_reference)
    create_reference_book(book_reference)
    create_reference_article(article_reference)
    create_reference_inproceeding(inproceeding_reference)
    return redirect("/")


# Route for resetting the database (testing only)
if test_env:
    @app.route("/reset_db")
    def reset_database():
        reset_db()
        return jsonify({'message': "db reset"})
