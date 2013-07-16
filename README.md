todos-app
=========

A simple "Todo" app using Django for students and faculty of OSU IT.

This is a port of [TodosMVC.com](http://todosmvc.com) to Django with some added Ajax and accounts.

## accounts
This module provides form overrides for django.contrib.auth to use an email field for the username in the create user and login forms, in addition to the url patterns and views to login, logout and create an account.

## auth_backend
This module provides and override for django.contrib.auth to check for an email address first, falling back to a username.

## db
Holds your local SQLite database so you don't overwrite other people's data.

## lib
Provides a common place to put classes that are shared across modules.

## static
This directory is where Django will collect static media from your project and 3rd party projects to for deployment.

## static-assets
This is where you keep static media that you are creating, such as images, less, css, js, fonts, etc.

## templates
All of the HTML templates used by the views live here, and extend a common base template.

## todos
This module holds the Todo model class, views, urls and forms for everything related to Todos.

## todos_app
This module holds our root urls, project settings and wsgi application definition.

### pip
A requirements.txt is provided for easy installation of dependencies into a virtualenv or in production.

### manage.py
Is django's built-in management command utility. This is used for starting up a local server to execute our code and much, much more.

### How to run this project:

These are the bare-minium instructions for running this code. These instructions assume you have Python 2.6.x or higher installed on your development computer. Django 1.5.x has experimental support for Python 3, but I would recommend staying with Python 2.7.x

First, you'll need to clone this repo to your local machine. Then create a SQLite database for the project to use. I would recommend using the SQLite Management Tool in Firefox. Name the database "todos.sqlite" and save it to the db folder in the project.

Next you'll want to get the project dependencies installed via Pip. See: https://pypi.python.org/pypi/pip for more information on PIP, and also these instructions for installation for Python and friends:

OS X: http://docs.python-guide.org/en/latest/starting/install/osx.html

Windows: http://docs.python-guide.org/en/latest/starting/install/win.html

Linux: http://docs.python-guide.org/en/latest/starting/install/linux.html

Once you have PIP installed, you'll want to:

    $ cd [path-to-project]
    $ pip install -r requirements.txt

This will install all of the modules specified in requirements.txt into the *system* python path. This is fine if it's the only project you're working on. I would highly recommend using [virtualenv](https://virtualenv.readthedocs.org/en/latest/) and [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/) for working on multiple projects.

Now hat dependencies are installed, we can sync up the database:

    $ cd [path-to-project]
    $ python manage.py syncdb

This will create the default table structure for Django. We'll use [South](http://south.aeracode.org) to migrate our project-specific models.

    $ python manage.py migrate todos

This will run the migration files in: todos/migrations to create and modify the necessary tables for the "todos" app module.

At this point, we should be able to run the project:

    $ python manage.py runserver

This will start up an instance of the built-in Django web server running at: [http://localhost:8000](http://localhost:8000), and you should be at the login view. Since you don't have an account yet, follow the link to create an account, fill out the form, and you should be on your way to creating lots of interesting todos :)
