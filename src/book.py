class Book:
    def __init__(self, book_id, author, title, book_title, publisher, year):
        if not all([author, title, book_title, publisher, year]):
            raise ValueError(
                "All fields (author, title, book_title, publisher, year) are required.")
        self.id = book_id
        self.author = author
        self.title = title
        self.book_title = book_title
        self.publisher = publisher
        self.year = year

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year}), published by {self.publisher}. Book_title: {self.book_title}"
