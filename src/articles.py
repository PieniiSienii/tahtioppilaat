class Articles:
    def __init__(self, id, author, title, journal, year):
        if not all([author, title, journal, year]):
            raise ValueError("All fields (author, title, journal, year) are required.")
        self.id = id
        self.author = author
        self.title = title
        self.journal = journal
        self.year = year

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year}), journal: {self.journal}"
        