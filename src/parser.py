import bibtexparser
from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase

def create_bibtex(entrytype, contents):
    print("creating", entrytype)
    db = BibDatabase()
    entry = None

    if entrytype == "doi":
        # TODO
        return None
    
    elif entrytype == "book":
        print(contents)
        entry = {
            'ENTRYTYPE': entrytype,
            'ID': 'none',
            'author': contents[1],
            'title': contents[2],
            'booktitle': contents[3],
            'publisher': contents[4],
            'year': str(contents[5])
        }
    elif entrytype == "article":
        entry = {
            'ENTRYTYPE': entrytype,
            'ID': 'none',
            'author': contents[1],
            'title': contents[2],
            'journal': contents[3],
            'year': str(contents[4])
        }
    elif entrytype == "inproceeding":
        entry = {
            'ENTRYTYPE': entrytype,
            'ID': 'none',
            'author': contents[1],
            'title': contents[2],
            'booktitle': contents[3],
            'year': str(contents[4])
        }

    db.entries = [entry]
    writer = BibTexWriter()
    bibtex_string = writer.write(db)

    return bibtex_string

