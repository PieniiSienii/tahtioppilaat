class Inproceeding:
    # pylint: disable=too-many-positional-arguments
    def __init__(self, inproceeding_id, citation_key, author, title, booktitle, year):
        if not all([author, title, booktitle, year]):
            raise ValueError(
                "All fields (author, title, booktitle, year) are required.")
        self.id = inproceeding_id
        self.citation_key = citation_key
        self.author = author
        self.title = title
        self.booktitle = booktitle
        self.year = year

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year}). Book title: {self.booktitle}"
