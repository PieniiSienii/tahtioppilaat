## Tahtioppilaat
[![GHA workflow Badge](https://github.com/PieniiSienii/tahtioppilaat/workflows/CI/badge.svg)](https://github.com/Pieniisienii/tahtioppilaat/actions)
[![codecov](https://codecov.io/gh/PieniiSienii/tahtioppilaat/graph/badge.svg?token=0N8NYQEJWQ)](https://codecov.io/gh/PieniiSienii/tahtioppilaat)

[Backlog linkki](https://docs.google.com/spreadsheets/d/1tfCgtgHHC6YhraJJi992deDDh6dO0IaimUXH1h2Ntps/edit?gid=0#gid=0)

### Definition of done: 

Ohjelma toimii niin kuin user story kuvaa, koodia on testattu, jonka jälkeen löydetyt ongelmat korjattu.


### Käyttöohje:

1. **Kloonaa repositorio**:

```bash
git clone https://github.com/PieniiSienii/tahtioppilaat.git
```

2. **Lataa poetry**:

```bash
pip install poetry
```

3. **Lataa riippuvuudet**: 

```bash
poetry install
```

4. **Luo .env tiedosto, josta löytyy DATABASE_URL, TEST_ENV ja SECRET_KEY**:

```bash
DATABASE_URL=postgresql://<your_database_service>
TEST_ENV=true
SECRET_KEY=<your_own_secret>
```

5. **Luo virtuaaliympäristö**:

```bash
poetry shell
```

6. **Käynnistä ohjelma**:

```bash
python3 src/index.py
```
