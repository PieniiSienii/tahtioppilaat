class Book:
    # pylint: disable=too-many-positional-arguments
    def __init__(self, book_id, citation_key, author, title, booktitle, publisher, year):
        if not all([author, title, booktitle, publisher, year]):
            raise ValueError(
                "All fields (author, title, booktitle, publisher, year) are required.")
        self.id = book_id
        self.citation_key = citation_key
        self.author = author
        self.title = title
        self.booktitle = booktitle
        self.publisher = publisher
        self.year = year

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year}), " + \
           f"published by {self.publisher}. Book title: {self.booktitle}"
