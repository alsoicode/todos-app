todos-app
=========

A simple "Todo" app using Django for students and faculty of OSU IT.

This is a port of TodosMVC.com to Django with some added Ajax and accounts.

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
