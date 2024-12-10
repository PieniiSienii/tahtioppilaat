class Unpublished:
    # pylint: disable=too-many-positional-arguments
    def __init__(self, unpublished_id, citation_key, author, title, note):
        if not all([author, title, note]):
            raise ValueError(
                "All fields (author, title, note) are required.")
        self.id = unpublished_id
        self.citation_key = citation_key
        self.author = author
        self.title = title
        self.note = note

    def __str__(self):
        return f"{self.title} by {self.author}, {self.note}"