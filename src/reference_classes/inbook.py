class Inbook:
    # pylint: disable=too-many-positional-arguments
    def __init__(self, inbook_id, citation_key, author, title, chapter, publisher, year):
        if not all([author, title, chapter, publisher, year]):
            raise ValueError(
                "All fields (author, title, chapter, publisher, year) are required.")
        self.id = inbook_id
        self.citation_key = citation_key
        self.author = author
        self.title = title
        self.chapter = chapter
        self.publisher = publisher
        self.year = year

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year}), " + \
               f"chapter: {self.chapter}, published by {self.publisher}"