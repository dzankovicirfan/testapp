# Testapp

#### App for scraping website with python 3, django with beautifulsoup4 and pillow

  Set up on heroku optional


## Installation

Activate virtual enviroment.
Install the dependecies.

    $ pip install -r requirements.txt
    $ python manage.py migrate
    $ python manage.py makemigrations


## Run scraper

parse_trainee is mannagment command that is going to scrape "https://www.trainee.de/traineestellen/" page, and parse data in python objects and write it in database. Database is PostgreSQL.

    $ python manage.py parse_trainee
