import unittest
import re

class TestDOIValidation(unittest.TestCase):
    def setUp(self):
        # This could contain any setup needed before each test
        pass
    
    def validate_doi_url(self, url):
        """Helper method to validate DOI URL format"""
        doi_pattern = r'^https?://(dx\.)?doi\.org/10\.\d{4,9}/[-._;()/:\w]+$'
        return bool(re.match(doi_pattern, url))

    def test_valid_doi_links(self):
        """Test that valid DOI URLs are accepted"""
        valid_urls = [
            "https://doi.org/10.1234/567890",
            "http://doi.org/10.1234/journal.article",
            "https://dx.doi.org/10.5678/abcdef",
            "http://dx.doi.org/10.1234/test-123"
        ]
        
        for url in valid_urls:
            with self.subTest(url=url):
                self.assertTrue(
                    self.validate_doi_url(url),
                    f"URL should be valid: {url}"
                )

    def test_invalid_doi_links(self):
        """Test that invalid DOI URLs are rejected"""
        invalid_urls = [
            "",  # empty string
            "not a url",  # plain text
            "http://example.com",  # wrong domain
            "https://doi.org/",  # missing DOI
            "https://doi.org/11.1234/test",  # wrong DOI prefix
            "https://doi.org/10.123/test",  # publisher ID too short
            "http://doi.org/10.1234/$$$",  # invalid characters
            "doi.org/10.1234/test"  # missing protocol
        ]
        
        for url in invalid_urls:
            with self.subTest(url=url):
                self.assertFalse(
                    self.validate_doi_url(url),
                    f"URL should be invalid: {url}"
                )

    def test_doi_starts_with_10(self):
        """Test that DOI must start with '10.'"""
        invalid_url = "https://doi.org/11.1234/test"
        self.assertFalse(
            self.validate_doi_url(invalid_url),
            "DOI must start with '10.'"
        )

    def test_doi_has_valid_publisher_id(self):
        """Test that publisher ID is valid (4-9 digits)"""
        # Test too short publisher ID
        short_id_url = "https://doi.org/10.123/test"
        self.assertFalse(
            self.validate_doi_url(short_id_url),
            "Publisher ID should be at least 4 digits"
        )
        
        # Test valid publisher ID
        valid_id_url = "https://doi.org/10.1234/test"
        self.assertTrue(
            self.validate_doi_url(valid_id_url),
            "Publisher ID of 4 digits should be valid"
        )
