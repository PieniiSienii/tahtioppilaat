import subprocess

class DOI:
    def __init__(self, doi_id, doi):
        self.id = doi_id
        self.doi = doi

    def __str__(self):
        return f"{self.doi}"

    
    def convert_to_bibtex(self):
        # Use subprocess to call the 'doi2bib' command
        try:
            result = subprocess.run(
                ['doi2bib', self.doi],
                check=True,  # Raise an exception if the command fails
                stdout=subprocess.PIPE,  # Capture the standard output
                stderr=subprocess.PIPE  # Capture the standard error
            )
            # Return the BibTeX result
            return result.stdout.decode('utf-8')  # Convert bytes to string
        except subprocess.CalledProcessError as e:
            print(f"Error: {e.stderr.decode('utf-8')}")
            return None

# Create a DOI object
doi = DOI("1", "10.1038/s41524-017-0032-0")

# Get the BibTeX entry for the DOI
bibtex = doi.convert_to_bibtex()

# Print the BibTeX entry
if bibtex:
    print(bibtex)
else:
    print("Failed to fetch BibTeX entry.")
