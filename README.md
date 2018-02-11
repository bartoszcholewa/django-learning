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

# Chapter 4
1. Creating login/loggout views
2. Creating authentification view
3. Creating changing/reseting password view
4. Creating registration user view
5. Using messages framework

# Chapter 5
1. Creating "Image" model
2. Many-to-Many relations
3. Registering "Image" in admin panel
4. Placing images from other sites
5. Creating detail view from image
6. Creating thumbnail using sorl
7. AJAX, jQuery, JavaScript
8. WIP...