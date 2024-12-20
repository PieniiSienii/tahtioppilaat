class Misc:
    def __init__(self, misc_id, citation_key):
        self.id = misc_id
        self.citation_key = citation_key

    def __str__(self):
        return f"Misc reference {self.citation_key}"