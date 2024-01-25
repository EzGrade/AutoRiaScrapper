# AutoRiaScrapper
## Usage

### Install dependencies
```bash
pip install -r requirements.txt
```

### Run
```bash
python src/Scrapper/auto_runner.py
```

### Run django admin
```bash
python src/AutoRia/manage.py runserver
```

### .env file
```bash
# .env file
# Path: src/AutoRia/.env
# Variables:
#   - TIME - time in seconds, day time to run scrapper
#   - HEADLESS - True or False, run browser in headless mode
#   - DATABASE_NAME - name of database
#   - DATABASE_USER - user of database
#   - DATABASE_PASSWORD - password of database
#   - DATABASE_HOST - host of database
#   - DATABASE_PORT - port of database
```

### Database
Project uses PostgreSQL database. You can change database configuration in .env file.

## Project structure
```
AutoRiaScrapper
├── README.md
├── requirements.txt
├── dumps
└── src
    ├── AutoRia
    │   ├── __init__.py
    │   ├── __pycache__
    │   ├── admin.py
    │   ├── apps.py
    │   ├── migrations
    │   ├── models.py
    │   ├── tests.py
    │   ├── urls.py
    │   ├── views.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    └── Scrapper
        ├── __init__.py
        ├── __pycache__
        ├── auto_runner.py
        ├── auto_runner.sh
        ├── auto_runner.service
        ├── auto_runner.timer
        ├── config.py
        ├── db.py
        ├── logger.py
        ├── models.py
        ├── parser.py
        ├── settings.py
        ├── urls.py
        └── utils.py
```
### Main files and folders
- **dumps** - folder with dumps of database
- **src/AutoRia** - django project
- **src/Scrapper** - scrapper package
- **src/Scrapper/main.py** - main file of scrapper
- **src/Scrapper/auto_runner.py** - file to run scrapper

# Project stack
- Python 3.12
- Django 5.0.1
- Selenium 4.17.2
- bs4 0.0.2