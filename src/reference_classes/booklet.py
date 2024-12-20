class Booklet:
    def __init__(self, booklet_id, citation_key, title):
        if not title:
            raise ValueError("Title is required.")
        self.id = booklet_id
        self.citation_key = citation_key
        self.title = title

    def __str__(self):
        return f"{self.title}"