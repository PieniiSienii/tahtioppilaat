class Mastersthesis:
    # pylint: disable=too-many-positional-arguments
    def __init__(self, thesis_id, citation_key, author, title, school, year):
        if not all([author, title, school, year]):
            raise ValueError(
                "All fields (author, title, school, year) are required.")
        self.id = thesis_id
        self.citation_key = citation_key
        self.author = author
        self.title = title
        self.school = school
        self.year = year

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year}), {self.school}"