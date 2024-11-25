import unittest
from book import Book
from article import Article
from inproceeding import Inproceeding  # adjust import path as needed

class TestBook(unittest.TestCase):
    def test_valid_book_creation(self):
        book = Book(1, "John Doe", "Test Book", "Book Collection", "Test Publisher", 2024)
        self.assertEqual(book.author, "John Doe")
        self.assertEqual(book.title, "Test Book")
        self.assertEqual(book.book_title, "Book Collection")
        self.assertEqual(book.publisher, "Test Publisher")
        self.assertEqual(book.year, 2024)
        
    def test_book_missing_fields(self):
        with self.assertRaises(ValueError):
            Book(1, "", "Test Book", "Book Collection", "Test Publisher", 2024)
        with self.assertRaises(ValueError):
            Book(1, "John Doe", "", "Book Collection", "Test Publisher", 2024)
            
    def test_book_string_representation(self):
        book = Book(1, "John Doe", "Test Book", "Book Collection", "Test Publisher", 2024)
        expected = "Test Book by John Doe (2024), published by Test Publisher. Book_title: Book Collection"
        self.assertEqual(str(book), expected)

class TestArticle(unittest.TestCase):
    def test_valid_article_creation(self):
        article = Article(1, "Jane Smith", "Test Article", "Science Journal", 2024)
        self.assertEqual(article.author, "Jane Smith")
        self.assertEqual(article.title, "Test Article")
        self.assertEqual(article.journal, "Science Journal")
        self.assertEqual(article.year, 2024)
        
    def test_article_missing_fields(self):
        with self.assertRaises(ValueError):
            Article(1, "", "Test Article", "Science Journal", 2024)
        with self.assertRaises(ValueError):
            Article(1, "Jane Smith", "", "Science Journal", 2024)
            
    def test_article_string_representation(self):
        article = Article(1, "Jane Smith", "Test Article", "Science Journal", 2024)
        expected = "Test Article by Jane Smith (2024), journal: Science Journal"  # Updated format
        self.assertEqual(str(article), expected)

class TestInproceeding(unittest.TestCase):
    def test_valid_inproceeding_creation(self):
        inproceeding = Inproceeding(1, "Alice Brown", "Test Paper", "Conference Proceedings", 2024)
        self.assertEqual(inproceeding.author, "Alice Brown")
        self.assertEqual(inproceeding.title, "Test Paper")
        self.assertEqual(inproceeding.book_title, "Conference Proceedings")
        self.assertEqual(inproceeding.year, 2024)
        
    def test_inproceeding_missing_fields(self):
        with self.assertRaises(ValueError):
            Inproceeding(1, "", "Test Paper", "Conference Proceedings", 2024)
        with self.assertRaises(ValueError):
            Inproceeding(1, "Alice Brown", "", "Conference Proceedings", 2024)
            
    def test_inproceeding_string_representation(self):
        inproceeding = Inproceeding(1, "Alice Brown", "Test Paper", "Conference Proceedings", 2024)
        expected = "Test Paper by Alice Brown (2024). Book_title: Conference Proceedings"  # Updated format
        self.assertEqual(str(inproceeding), expected)

class TestIntegration(unittest.TestCase):
    def test_different_reference_types(self):
        book = Book(1, "John Doe", "Test Book", "Book Collection", "Test Publisher", 2024)
        article = Article(2, "Jane Smith", "Test Article", "Science Journal", 2024)
        inproceeding = Inproceeding(3, "Alice Brown", "Test Paper", "Conference Proceedings", 2024)
        
        # Updated string checks to match actual formats
        self.assertIn("published by", str(book))
        self.assertIn("journal:", str(article))  # Updated check
        self.assertIn("Book_title:", str(inproceeding))  # Updated check

if __name__ == '__main__':
    unittest.main(verbosity=2)