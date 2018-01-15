# Django by Exaple - Antonio Melé [packt]
Based on book of Antonio Melé -  Django By Exaple

# Chapter 1
* Django version check
    $ python
    >>> import django
    >>> django.VERSION

* Creating new project
    $ django-admin startproject mysite

* Creating new app
    $ python manage.py startapp blog

* Migrating new app
    $ python manage.py makemigrations blog
    $ python manage.py sqlmigrate blog 0001 #checking without commiting
    $ python manage.py migrate

* Adding superuser
    $ python manage.py createsuperuser

* Running server
    $ python manage.py runserver