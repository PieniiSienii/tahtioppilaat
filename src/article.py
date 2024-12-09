class Article:
    # pylint: disable=too-many-positional-arguments
    def __init__(self, article_id, citation_key, author, title, journal, year):
        if not all([author, title, journal, year]):
            raise ValueError(
                "All fields (author, title, journal, year) are required.")
        self.id = article_id
        self.citation_key = citation_key
        self.author = author
        self.title = title
        self.journal = journal
        self.year = year

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year}), journal: {self.journal}"
