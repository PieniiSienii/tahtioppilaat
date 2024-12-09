class Book:
    # pylint: disable=too-many-positional-arguments
    def __init__(self, book_id, citation_key, author, title, book_title, publisher, year):
        if not all([citation_key, author, title, book_title, publisher, year]):
            raise ValueError(
                "All fields (author, title, book_title, publisher, year) are required.")
        self.id = book_id
        self.citation_key = citation_key
        self.author = author
        self.title = title
        self.book_title = book_title
        self.publisher = publisher
        self.year = year

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year}), " + \
           f"published by {self.publisher}. Book_title: {self.book_title}"
