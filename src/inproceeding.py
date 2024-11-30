class Inproceeding:
    def __init__(self, inproceeding_id, author, title, book_title, year):
        if not all([author, title, book_title, year]):
            raise ValueError(
                "All fields (author, title, book_title, year) are required.")
        self.id = inproceeding_id
        self.author = author
        self.title = title
        self.book_title = book_title
        self.year = year

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year}). Book_title: {self.book_title}"
