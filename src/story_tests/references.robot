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

Add by DOI and delete
    Go To  ${HOME_URL}
    Click Element  add_by_doi
    Input Text  doi  abcdefg
    Click Button  Add Reference
    Page Should Contain  abcdefg
    
    #Delete
    Click Element  xpath=//button[text()='Delete']
    Handle Alert  ACCEPT
    Sleep  0.4s
    Page Should Not Contain  abcdefg

Add Article
    Go To  ${HOME_URL}
    Click Element  add_article
    Input Text  article_author  author1
    Input Text  article_title  title1
    Input Text  article_journal  journal1
    Input Text  article_year  2024

    Click Button  Add Reference
    Page Should Contain  title1 by author1 (2024), journal: journal1
    
    #Delete
    Click Element  xpath=//button[text()='Delete']
    Handle Alert  ACCEPT
    Sleep  0.4s
    Page Should Not Contain  author1

Add Conference Paper
    Go To  ${HOME_URL}
    Click Element  add_conference_paper
    Input Text  inproceeding_author  author1
    Input Text  inproceeding_title  title1
    Input Text  inproceeding_book_title  booktitle1
    Input Text  inproceeding_year  2024

    Click Button  Add Reference
    Page Should Contain  title1 by author1 (2024). Book_title: booktitle1
    
    #Delete
    Click Element  xpath=//button[text()='Delete']
    Handle Alert  ACCEPT
    Sleep  0.4s
    Page Should Not Contain  author1

Add Book
    Go To  ${HOME_URL}
    Click Element  add_book
    Input Text  book_author  author1
    Input Text  book_title  title1
    Input Text  book_book_title  booktitle1
    Input Text  book_publisher  publisher1
    Input Text  book_year  2024

    Click Button  Add Reference
    Page Should Contain  title1 by author1 (2024), published by publisher1. Book_title: booktitle1

    #Delete
    Click Element  xpath=//button[text()='Delete']
    Handle Alert  ACCEPT
    Sleep  0.4s
    Page Should Not Contain  author1
