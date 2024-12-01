from flask import redirect, render_template, request, jsonify
from db_helper import reset_db
from repositories.todo_repository import get_books, create_reference_doi,\
create_reference_book, create_reference_article,\
create_reference_inproceeding, get_dois, get_articles, get_inproceedings, \
delete_doi, delete_book, delete_article, delete_inproceeding, \
update_doi, update_book, update_article, update_inproceeding
from config import app, test_env

@app.route("/", methods=["POST", "GET"])
def index():
    # Fetch dois (or references) from the database
    dois = get_dois()
    # return render_template("index.html", dois=dois)  # Pass 'dois' instead of 'doi'
    # Fetch books (or references) from the database
    books = get_books()
    articles = get_articles()
    inproceedings = get_inproceedings()
    # Pass 'dois' instead of 'doi'
    return render_template("index.html", books=books,\
                            dois=dois,\
                            articles=articles,\
                            inproceedings=inproceedings)


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

@app.route("/delete_reference/<reference_type>/<int:reference_id>", methods=["POST"])
def delete_reference(reference_type, reference_id):
    if reference_type == "doi":
        delete_doi(reference_id)
    elif reference_type == "book":
        delete_book(reference_id)
    elif reference_type == "article":
        delete_article(reference_id)
    elif reference_type == "inproceeding":
        delete_inproceeding(reference_id)
    return redirect("/")

@app.route("/edit_reference/<reference_type>/<int:reference_id>", methods=["POST"])
def edit_reference(reference_type, reference_id):
    if reference_type == "doi":
        update_doi(reference_id, request.form.get("doi"))
    elif reference_type == "book":
        update_book(reference_id, {
            "author": request.form.get("book_author"),
            "title": request.form.get("book_title"),
            "book_title": request.form.get("book_book_title"),
            "publisher": request.form.get("book_publisher"),
            "year": request.form.get("book_year")
        })
    elif reference_type == "article":
        update_article(reference_id, {
            "author": request.form.get("article_author"),
            "title": request.form.get("article_title"),
            "journal": request.form.get("article_journal"),
            "year": request.form.get("article_year")
        })
    elif reference_type == "inproceeding":
        update_inproceeding(reference_id, {
            "author": request.form.get("inproceeding_author"),
            "title": request.form.get("inproceeding_title"),
            "book_title": request.form.get("inproceeding_book_title"),
            "year": request.form.get("inproceeding_year")
        })
    return redirect("/")
