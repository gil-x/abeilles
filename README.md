# Abeilles Aide et Entraide

Django web app for *Abeilles Aide et Entraide* association.

___


## 1. Features
...
___


## 2. Tech

### 2.1 Requirements
- Python 3.6

### 2.2 Stack
- Django 3
- Django-template
- CSS3
- JavaScript vanilla
- sqlite3
___


## 3. Install (Linux)

### 3.1 Locally

1. Clone project, move into **abeilles** folder

2. Create a Python [virtual environnement](https://docs.python.org/3/library/venv.html) and activate it:

        python -m venv venv
        . venv/bin/activate

3. Install dependencies:

        pip install -r requirements.txt

4. Copy **abeilles/settings_specific_sample.py** as **abeilles/settings_specific.py**

5. Update database:

        python manage.py migrate

6. Run local server:

        python manage.py runserver

### 3.2 Create account

1. Be sure **venv** is started and at project root run:
    
        manage.py createsuperuser

2. Respond...

3. Now you can login at [0.0.0.0:8000/admin/](http://0.0.0.0:8000/admin/)

### 3.3 Populate

Data are provided in order to populate database.

Script delete **all** existing content and users,
contains also *admin* accounts with very low passwords,
so...

**DO NOT EVER USE POPULATE SCRIPT IN PRODUCTION**!

Be also cautious to remove any admin accounts
when copying data from instance to another.

1. Activate venv and:

        manage.py populate

2. script is [here](services/management/commands/populate.py)

### 3.4 Troubleshooting

- if something goes wrong with database and if you don't give a shit about your content, just delete db.sqlite3 file, then:

        manage.py migrate
        manage.py populate
