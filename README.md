# AutoRiaScrapper

## Usage

### Install dependencies

```bash
pip install -r requirements.txt
```

### Make migrations

```bash
python src/AutoRia/manage.py makemigrations
python src/AutoRia/manage.py migrate
```

### Run Scheduled Scrapper

```bash
python src/Scrapper/auto_runner.py
```

### Or

### Run Scrapper

```bash
python src/Scrapper/main.py
```

### Run django admin (optional)

If you want to run django admin, you need to create superuser.

```bash
python src/AutoRia/manage.py createsuperuser
```

Then you can run django admin.

```bash
python src/AutoRia/manage.py runserver
```

Now you can visit 127.0.0.1:8000/admin.

For authorization you need to use superuser credentials.

### .env file

## Warning!

- Setting DELAY less than 0.5 second can lead to losing data.
- Setting TIME works only on next minute. So if currently is 12:00,
  and you set TIME as 12:00 it will run only tomorrow at 12:00. So that you need to set it on next minute.

```bash
# .env file
# Path: src/.env
# Variables:
#   - TIME - time in seconds, day time to run scrapper
#   - DELAY - time in seconds, delay to parse data from page
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