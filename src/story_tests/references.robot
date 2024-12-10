*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset References

*** Test Cases ***
Page loads empty
    Go To  ${HOME_URL}
    Title Should Be  My Bibliography Manager
    Page Should Contain  Manage your scientific references with ease. Select your preferred input method below.

Add by DOI, BibTeX, edit and delete
    Go To  ${HOME_URL}
    Click Element  add_by_doi
    Input Text  doi  10.1145/1968.1972
    Click Button  Add Reference
    Page Should Contain  10.1145/1968.1972

    #BibTeX
    Click Element  xpath=//button[text()='BibTeX']
    Sleep  3s
    Page Should Contain  @article{Valiant_1984, title={A theory of the learnable}, volume={27}, ISSN={1557-7317}, url={http://dx.doi.org/10.1145/1968.1972}\, DOI={10.1145/1968.1972}, number={11}, journal={Communications of the ACM}, publisher={Association for Computing Machinery (ACM)}, author={Valiant, L. G.}, year={1984}, month=nov, pages={1134–1142} }


    #Edit
    Click Element  xpath=//button[text()='Edit']
    Input Text  doi  gfedcba
    Click Button  Add Reference
    Page Should Contain  gfedcba

    #Delete
    Click Element  xpath=//button[text()='Delete']
    Handle Alert  ACCEPT
    Sleep  3s
    Page Should Not Contain  gfedcba

Add Article, BibTeX, edit and delete
    Go To  ${HOME_URL}
    Click Element  add_article
    Input Text  article_author  author1
    Input Text  article_title  title1
    Input Text  article_journal  journal1
    Input Text  article_year  2024

    Click Button  Add Reference
    Page Should Contain  title1 by author1 (2024), journal: journal1

    #BibTeX
    Click Element  xpath=//button[text()='BibTeX']
    Sleep  3s
    Page Should Contain  @article{,
    Page Should Contain  author = {author1},
    Page Should Contain  journal = {journal1},
    Page Should Contain  title = {title1},
    Page Should Contain  year = {2024}

    #Edit
    Click Element  xpath=//button[text()='Edit']
    Input Text  article_author  author2
    Input Text  article_title  title2
    Input Text  article_journal  journal2
    Input Text  article_year  2023
    Click Button  Add Reference
    Page Should Contain  title2 by author2 (2023), journal: journal2
    
    #Delete
    Click Element  xpath=//button[text()='Delete']
    Handle Alert  ACCEPT
    Sleep  3s
    Page Should Not Contain  author1

Add Conference Paper, BibTeX, edit and delete
    Go To  ${HOME_URL}
    Click Element  add_conference_paper
    Input Text  inproceeding_author  author1
    Input Text  inproceeding_title  title1
    Input Text  inproceeding_book_title  booktitle1
    Input Text  inproceeding_year  2024

    Click Button  Add Reference
    Page Should Contain  title1 by author1 (2024). Book_title: booktitle1

    #BibTeX
    Click Element  xpath=//button[text()='BibTeX']
    Sleep  3s
    Page Should Contain  @inproceeding{,
    Page Should Contain  author = {author1},
    Page Should Contain  booktitle = {booktitle1},
    Page Should Contain  title = {title1},
    Page Should Contain  year = {2024}

    #Edit
    Click Element  xpath=//button[text()='Edit']
    Input Text  inproceeding_author  author2
    Input Text  inproceeding_title  title2
    Input Text  inproceeding_book_title  booktitle2
    Input Text  inproceeding_year  2023
    Click Button  Add Reference
    Page Should Contain  title2 by author2 (2023). Book_title: booktitle2
    
    #Delete
    Click Element  xpath=//button[text()='Delete']
    Handle Alert  ACCEPT
    Sleep  3s
    Page Should Not Contain  author1

Add Book, BibTeX, edit and delete
    Go To  ${HOME_URL}
    Click Element  add_book
    Input Text  book_author  author1
    Input Text  book_title  title1
    Input Text  book_book_title  booktitle1
    Input Text  book_publisher  publisher1
    Input Text  book_year  2024

    Click Button  Add Reference
    Page Should Contain  title1 by author1 (2024), published by publisher1. Book_title: booktitle1

    #BibTeX
    Click Element  xpath=//button[text()='BibTeX']
    Sleep  3s
    Page Should Contain  @book{,
    Page Should Contain  author = {author1},
    Page Should Contain  booktitle = {booktitle1},
    Page Should Contain  publisher = {publisher1},
    Page Should Contain  title = {title1},
    Page Should Contain  year = {2024}

    #Edit
    Click Element  xpath=//button[text()='Edit']
    Input Text  book_author  author2
    Input Text  book_title  title2
    Input Text  book_book_title  booktitle2
    Input Text  book_publisher  publisher2
    Input Text  book_year  2023
    Click Button  Add Reference
    Page Should Contain  title2 by author2 (2023), published by publisher2. Book_title: booktitle2

    #Delete
    Click Element  xpath=//button[text()='Delete']
    Handle Alert  ACCEPT
    Sleep  3s
    Page Should Not Contain  author1
