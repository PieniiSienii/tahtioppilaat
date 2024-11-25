*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset Todos

*** Test Cases ***
At start there are no todos
    Go To  ${HOME_URL}
    Title Should Be  My Bibliography Manager
    Page Should Contain  Manage your scientific references with ease. Select your preferred input method below.

Add by DOI
    Go To  ${HOME_URL}
    Click Element  add_by_doi
    Input Text  doi  abcdefg
    Click Button  Add Reference
    Page Should Contain  abcdefg

Add Article
    Go To  ${HOME_URL}
    Click Element  add_article
    Input Text  article_author  author1
    Input Text  article_title  title1
    Input Text  article_journal  journal1
    Input Text  article_year  2024

    Click Button  Add Reference
    Page Should Contain  title1 by author1 (2024), journal: journal1

Add Conference Paper
    Go To  ${HOME_URL}
    Click Element  add_conference_paper
    Input Text  inproceeding_author  author1
    Input Text  inproceeding_title  title1
    Input Text  inproceeding_book_title  booktitle1
    Input Text  inproceeding_year  2024

    Click Button  Add Reference
    Page Should Contain  title1 by author1 (2024). Book_title: booktitle1

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

After adding two todos and marking one done, there is one unfinished
    Go To  ${HOME_URL}
    Click Link  Create new todo
    Input Text  content  Buy milk
    Click Button  Create
    Click Link  Create new todo
    Input Text  content  Clean house
    Click Button  Create
    Click Button  //li[div[contains(text(), 'Buy milk')]]/form/button
    Page Should Contain  things still unfinished: 1
    Page Should Contain  Buy milk, done
