# function validateForm() {
#     const doi = document.getElementById('doi').value.trim();

#     // Article fields
#     const articleAuthor = document.getElementById('article_author').value.trim();
#     const articleTitle = document.getElementById('article_title').value.trim();
#     const articleJournal = document.getElementById('article_journal').value.trim();
#     const articleYear = document.getElementById('article_year').value.trim();

#     // Inproceedings fields
#     const inproceedingAuthor = document.getElementById('inproceeding_author').value.trim();
#     const inproceedingTitle = document.getElementById('inproceeding_title').value.trim();
#     const inproceedingBookTitle = document.getElementById('inproceeding_book_title').value.trim();
#     const inproceedingYear = document.getElementById('inproceeding_year').value.trim();

#     // Book fields
#     const bookAuthor = document.getElementById('book_author').value.trim();
#     const bookTitle = document.getElementById('book_title').value.trim();
#     const bookBookTitle = document.getElementById('book_book_title').value.trim();
#     const bookPublisher = document.getElementById('book_publisher').value.trim();
#     const bookYear = document.getElementById('book_year').value.trim();

#     // Check if DOI is provided
#     if (doi !== '') {
#         return true;
#     }

#     // Check if all fields in any section are filled
#     const isArticleComplete = articleAuthor !== '' && articleTitle !== '' &&
#                             articleJournal !== '' && articleYear !== '';

#     const isinproceedingComplete = inproceedingAuthor !== '' && inproceedingTitle !== '' &&
#                            inproceedingBookTitle !== '' && inproceedingYear !== '';

#     const isBookComplete = bookAuthor !== '' && bookTitle !== '' &&
#                          bookPublisher !== '' && bookYear !== '';

#     if (!isArticleComplete && !isInproceedingComplete && !isBookComplete) {
#         alert('Please either provide a DOI or fill in all fields for one type of reference.');
#         return false;
#     }

#     return true;
# }
