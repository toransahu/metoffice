# metoffice
Data visualisation - MetOffice

**Pre-requisites**
* Python 3.x
* Django > 1.4

**Steps to run:**

1. Install requirements:
```
pip install -r requirement.txt
```
2. Run server:
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
3. Load data to ORM:
https://127.0.0.1:8000/metoffice/load

4. View graphs
https://127.0.0.1:8000/metoffice/climate
