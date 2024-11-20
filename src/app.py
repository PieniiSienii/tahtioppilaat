from flask import redirect, render_template, request, jsonify, flash
from db_helper import reset_db
from repositories.todo_repository import get_books, create_reference
from config import app, test_env
from util import validate_todo

@app.route("/", methods=["POST", "GET"])
def index():
    # Fetch books (or references) from the database
    books = [i.doi for i in get_books()]
    return render_template("index.html", dois=books)  # Pass 'dois' instead of 'doi'


@app.route("/create_reference", methods=["POST", "GET"])
def reference_creation():
    # Get the reference link from the form
    reference_link = request.form.get("doi")

    try:
        # Validate and save the reference
        validate_todo(reference_link)  # Assuming validate_todo can handle reference validation
        create_reference(reference_link)
        return redirect("/")
    except Exception as error:
        flash(str(error))
        return redirect("/")


# Route for resetting the database (testing only)
if test_env:
    @app.route("/reset_db")
    def reset_database():
        reset_db()
        return jsonify({'message': "db reset"})
