class Techreport:
    # pylint: disable=too-many-positional-arguments
    def __init__(self, report_id, citation_key, author, title, institution, year):
        if not all([author, title, institution, year]):
            raise ValueError(
                "All fields (author, title, institution, year) are required.")
        self.id = report_id
        self.citation_key = citation_key
        self.author = author
        self.title = title
        self.institution = institution
        self.year = year

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year}), {self.institution}"