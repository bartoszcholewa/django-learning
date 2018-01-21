# Django by Exaple - Antonio Melé [packt]
Based on book of Antonio Melé -  Django By Exaple

# Usefull commands
* Django version check
```
    $ python
    >>> import django
    >>> django.VERSION
```

* Creating new project
```
    $ django-admin startproject mysite
```

* Creating new app
```
    $ python manage.py startapp blog
```

* Migrating new app
```
    $ python manage.py makemigrations blog
    $ python manage.py sqlmigrate blog 0001 #checking without commiting
    $ python manage.py migrate
```

* Adding superuser
```
    $ python manage.py createsuperuser
```

* Running server
```
    $ python manage.py runserver
```

# Chapter 1
1. Django Installation
2. Creating first project
3. Creating first app 'blog'
4. Creating admin site
5. QuerySet and menagers
6. Creating views
7. Creating templates
8. Creating pagination
9. Class based views

# Chapter 2
1. Creating blog post e-mail sharing function
2. Creating comments system
3. Creating tags function using django-taggit
4. Getting similar posts for recomendation

# Chapter 3
1. Creating own tags and filters
2. Adding sitemap
3. Adding RSS for blog posts