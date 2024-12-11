import bibtexparser
import subprocess
from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bparser import BibTexParser
from bibtexparser.customization import convert_to_unicode
from bibtexparser.bibdatabase import BibDatabase
from book import Book
from article import Article
from inproceeding import Inproceeding

def create_bibtex(entrytype, contents):
    print("creating", entrytype)
    db = BibDatabase()
    entry = None

    if entrytype == "doi":
        # TODO
        return None
    
    elif entrytype == "book":
        entry = {
            'ENTRYTYPE': entrytype,
            'ID': contents[1],
            'author': contents[2],
            'title': contents[3],
            'booktitle': contents[4],
            'publisher': contents[5],
            'year': str(contents[6])
        }
    elif entrytype == "article":
        entry = {
            'ENTRYTYPE': entrytype,
            'ID': contents[1],
            'author': contents[2],
            'title': contents[3],
            'journal': contents[4],
            'year': str(contents[5])
        }
    elif entrytype == "inproceeding":
        entry = {
            'ENTRYTYPE': entrytype,
            'ID': contents[1],
            'author': contents[2],
            'title': contents[3],
            'booktitle': contents[4],
            'year': str(contents[5])
        }

    db.entries = [entry]
    writer = BibTexWriter()
    bibtex_string = writer.write(db)

    return bibtex_string


def convert_to_bibtex(doi):
    # Use subprocess to call the 'doi2bib' command
    try:
        result = subprocess.run(
            ['doi2bib', doi],
            check=True,  # Raise an exception if the command fails
            stdout=subprocess.PIPE,  # Capture the standard output
            stderr=subprocess.PIPE  # Capture the standard error
        )
        # Return the BibTeX result
        bibtex_str = result.stdout.decode('utf-8')
        # print(extract_bibtex_fields(bibtex_str))
        return extract_bibtex_fields(bibtex_str)  # Convert bytes to string
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr.decode('utf-8')}")
        return None


def extract_bibtex_fields(bibtex_str):
    # Create a BibTeX parser
    parser = BibTexParser()
    parser.customization = convert_to_unicode
    
    # Parse the BibTeX string
    try:
        bib_database = bibtexparser.loads(bibtex_str, parser=parser)
    except Exception as e:
        print(f"Error parsing BibTeX: {e}")
        return None
    
    # Extract fields from the first entry (assuming there is at least one entry)
    if bib_database.entries:
        entry = bib_database.entries[0]
        # Define the fields you are interested in
        fields_of_interest = ['ENTRYTYPE', 'author', 'title', 'booktitle', 'year', 'journal', 'publisher']
        # Extract the fields
        extracted_fields = {field: entry.get(field, None) for field in fields_of_interest}
        
        for key, value in extracted_fields.items():
            if value is None:
                extracted_fields[key] = "no value"
        
        return extracted_fields
    else:
        print("No entries found in BibTeX data.")
        return None


def append_bibtex_entry(file_path, entry_str):
    with open(file_path, 'r') as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file)

    new_database = bibtexparser.loads(entry_str)

    bib_database.entries.extend(new_database.entries)

    writer = BibTexWriter()
    with open(file_path, 'w') as bibtex_file:
        bibtex_file.write(writer.write(bib_database))


def read_bibtex_file(file):
    with open(file) as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file)

    print(bib_database.entries)
