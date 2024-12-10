class Proceeding:
    def __init__(self, proceeding_id, citation_key, title, year):
        if not all([title, year]):
            raise ValueError(
                "All fields (title, year) are required.")
        self.id = proceeding_id
        self.citation_key = citation_key
        self.title = title
        self.year = year

    def __str__(self):
        return f"{self.title} ({self.year})"