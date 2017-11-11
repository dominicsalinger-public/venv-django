# venv-django

documentation: https://docs.djangoproject.com/en/1.11/intro/tutorial01/

1) install python 
    sudo apt install python
2) install pip
    sudo apt install python-pip
4) install virtualenv 
    sudo apt install virtualenv
5) create a virtual environment for django
    virtualenv venv-django
6) activate the virtualenv
    cd to venv-django; source bin/activate
7) install django
    pip install Django 
8) create a project
    django-admin startproject mysite
9) run django server
    cd to mysite; python manage.py runserver (can specify port with extra arg)
10) create an app within the project
    python manage.py startapp polls
11) edit views.py. each view corresponds with a method
12) create urls.py file to map the view to a url
13) point root URLconf at app.urls
