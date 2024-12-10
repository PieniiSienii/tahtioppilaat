class Incollection:
    # pylint: disable=too-many-positional-arguments
    def __init__(self, incollection_id, citation_key, author, title, booktitle, publisher, year):
        if not all([author, title, booktitle, publisher, year]):
            raise ValueError(
                "All fields (author, title, booktitle, publisher, year) are required.")
        self.id = incollection_id
        self.citation_key = citation_key
        self.author = author
        self.title = title
        self.booktitle = booktitle
        self.publisher = publisher
        self.year = year

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year}), " + \
               f"in {self.booktitle}, published by {self.publisher}"