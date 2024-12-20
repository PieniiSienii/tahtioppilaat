## Tahtioppilaat
[![GHA workflow Badge](https://github.com/PieniiSienii/tahtioppilaat/workflows/CI/badge.svg)](https://github.com/Pieniisienii/tahtioppilaat/actions)
[![codecov](https://codecov.io/gh/PieniiSienii/tahtioppilaat/graph/badge.svg?token=0N8NYQEJWQ)](https://codecov.io/gh/PieniiSienii/tahtioppilaat)

[Backlog linkki](https://docs.google.com/spreadsheets/d/1tfCgtgHHC6YhraJJi992deDDh6dO0IaimUXH1h2Ntps/edit?gid=0#gid=0) \
[Raportin linkki](https://docs.google.com/document/d/1hKblVI6xEbdoVMlVcHNgeIzqjhz6HfwkFmPojqSll0E/edit?tab=t.0)

Definition of done: 

Ohjelma toimii niin kuin user story kuvaa, koodia on testattu, jonka jälkeen löydetyt ongelmat korjattu.


Käyttöohje:

Kloonaa repositorio


Asenna poetry komennolla:
```
pip install poetry
```
Asenna seuraavaksi projektin riippuvuudet komennolla:
```
poetry install
```
Luo .env-tiedosto, josta löytyy DATABASE_URL, TEST_ENV ja SECRET_KEY, esimerkiksi:
```
DATABASE_URL=linkki_tietokantaan

TEST_ENV=true

SECRET_KEY=jokin_merkkijono
```
Käynnistä ohjelma komennolla:
```
poetry run invoke start
```
Tai voit siirtyä virtuaaliympäristöön komennolla:
```
poetry shell
```
ja sen jälkeen käynnistää ohjelman komennolla:
```
invoke start
```
