class Book:
    def __init__(self, author, title, booktitle, publisher, year):
        if not all([author, title, booktitle, publisher, year]):
            raise ValueError("All fields (author, title, booktitle, publisher, year) are required.")
        self.author = author
        self.title = title
        self.booktitle = booktitle
        self.publisher = publisher
        self.year = year
    
     def __str__(self):
        return f"{self.title} by {self.author} ({self.year}), published by {self.publisher}. Booktitle: {self.booktitle}"