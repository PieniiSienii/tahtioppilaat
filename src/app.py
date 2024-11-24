from flask import redirect, render_template, request, jsonify, flash
from db_helper import reset_db
from repositories.todo_repository import get_books, create_reference, get_dois
from config import app, test_env
from util import validate_todo

@app.route("/", methods=["POST", "GET"])
def index():
    # Fetch dois (or references) from the database
    dois = [i.doi for i in get_dois()]
    # return render_template("index.html", dois=dois)  # Pass 'dois' instead of 'doi'
    # Fetch books (or references) from the database
    books = get_books()
    return render_template("index.html", books=books, dois=dois)  # Pass 'dois' instead of 'doi'


# @app.route("/create_reference", methods=["POST", "GET"])
# def reference_creation():
#     # Get the reference link from the form
#     reference_link = request.form.get("doi")

#     try:
#         # Validate and save the reference
#         validate_todo(reference_link)  # Assuming validate_todo can handle reference validation
#         create_reference(reference_link)
#         return redirect("/")
#     except Exception as error:
#         flash(str(error))
#         return redirect("/")

@app.route("/create_reference", methods=["POST"])
def reference_creation():
    doi = request.form.get("doi")
    
    if doi:
        # Handle DOI case
        # Fetch metadata from DOI service
        validate_todo(doi)
        reference = doi
        #get doi metadata
        # reference = fetch_doi_metadata(doi)
    else:
        # Handle manual entry case
        reference = {
            "author": request.form.get("author"),
            "title": request.form.get("title"),
            "book_title": request.form.get("book_title"),
            "publisher": request.form.get("publisher"),
            "year": request.form.get("year")
        }
    # Save reference to database
    create_reference(reference)
    return redirect("/")




# Route for resetting the database (testing only)
if test_env:
    @app.route("/reset_db")
    def reset_database():
        reset_db()
        return jsonify({'message': "db reset"})
