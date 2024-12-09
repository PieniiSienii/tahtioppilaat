from flask import redirect, render_template, request, jsonify
from db_helper import reset_db
from repositories.todo_repository import get_books, create_reference_doi,\
create_reference_book, create_reference_article,\
create_reference_inproceeding, get_dois, get_articles, get_inproceedings, \
delete_doi, delete_book, delete_article, delete_inproceeding, \
update_doi, update_book, update_article, update_inproceeding, get_reference, \
get_all_references
from config import app, test_env
import parser
from flask import jsonify, Response

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
        "citation_key": request.form.get("book_citation_key"),
        "author": request.form.get("book_author"),
        "title": request.form.get("book_title"),
        "book_title": request.form.get("book_book_title"),
        "publisher": request.form.get("book_publisher"),
        "year": request.form.get("book_year")
    }
    article_reference = {
        "citation_key": request.form.get("article_citation_key"),
        "author": request.form.get("article_author"),
        "title": request.form.get("article_title"),
        "journal": request.form.get("article_journal"),
        "year": request.form.get("article_year")
    }
    inproceeding_reference = {
        "citation_key": request.form.get("inproceeding_citation_key"),
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
    match reference_type:
        case "doi":
            delete_doi(reference_id)
        case "book":
            delete_book(reference_id)
        case "article":
            delete_article(reference_id)
        case "inproceeding":
            delete_inproceeding(reference_id)
    return redirect("/")

@app.route("/edit_reference/<reference_type>/<int:reference_id>", methods=["POST"])
def edit_reference(reference_type, reference_id):
    match reference_type:
        case "doi":
            update_doi(reference_id, request.form.get("doi"))
        case "book":
            update_book(reference_id, {
                "citation_key": request.form.get("book_citation_key"),
                "author": request.form.get("book_author"),
                "title": request.form.get("book_title"),
                "book_title": request.form.get("book_book_title"),
                "publisher": request.form.get("book_publisher"),
                "year": request.form.get("book_year")
            })
        case "article":
            update_article(reference_id, {
                "citation_key": request.form.get("article_citation_key"),
                "author": request.form.get("article_author"),
                "title": request.form.get("article_title"),
                "journal": request.form.get("article_journal"),
                "year": request.form.get("article_year")
            })
        case "inproceeding":
            update_inproceeding(reference_id, {
                "citation_key": request.form.get("inproceeding_citation_key"),
                "author": request.form.get("inproceeding_author"),
                "title": request.form.get("inproceeding_title"),
                "book_title": request.form.get("inproceeding_book_title"),
                "year": request.form.get("inproceeding_year")
            })
    return redirect("/")


@app.route("/view_bibtex/<reference_type>/<int:reference_id>")
def view_bibtex(reference_type, reference_id):
    if reference_type == "doi":
        doi = get_reference(reference_type, reference_id)
        print(doi)
        bibtex = parser.convert_to_bibtex(doi.doi)  # Ensure doi.doi is passed, not the DOI object
        print(doi.doi)
    else:
        reference = get_reference(reference_type, reference_id)
        bibtex = parser.create_bibtex(reference_type, reference)
    
    return bibtex


@app.route("/export_all_bibtex", methods=["GET"])
def export_all_bibtex():
    try:
        # Get all references and separate them by type
        references = get_all_references()
        dois = references['dois']
        books = references['books']
        articles = references['articles']
        inproceedings = references['inproceedings']

        bibtex_entries = []
        
        # Process Books
        for book in books:
            # For books: ID, author, title, booktitle, publisher, year
            contents = [
                book.id,  # contents[0] - not used in create_bibtex
                article.citation_key,
                book.author,
                book.title,
                book.book_title,
                book.publisher,
                book.year
            ]
            entry = parser.create_bibtex('book', contents)
            if entry:
                bibtex_entries.append(entry)
        
        # Process Articles
        for article in articles:
            # For articles: ID, author, title, journal, year
            contents = [
                article.id,  # contents[0] - not used in create_bibtex
                article.citation_key,
                article.author,
                article.title,
                article.journal,
                article.year
            ]
            entry = parser.create_bibtex('article', contents)
            if entry:
                bibtex_entries.append(entry)
        
        # Process Inproceedings
        for inproceeding in inproceedings:
            # For inproceedings: ID, author, title, booktitle, year
            contents = [
                inproceeding.id,  # contents[0] - not used in create_bibtex
                article.citation_key,
                inproceeding.author,
                inproceeding.title,
                inproceeding.book_title,
                inproceeding.year
            ]
            entry = parser.create_bibtex('inproceeding', contents)
            if entry:
                bibtex_entries.append(entry)
        
        # DOIs are currently not implemented in parser
        
        if not bibtex_entries:
            return jsonify({"error": "No valid BibTeX entries could be created"}), 404
            
        combined_bibtex = '\n'.join(filter(None, bibtex_entries))
        return Response(combined_bibtex, mimetype='text/plain')
        
    except Exception as e:
        print(f"Error in export_all_bibtex: {str(e)}")
        import traceback
        print(traceback.format_exc())
        return jsonify({"error": str(e)}), 500
