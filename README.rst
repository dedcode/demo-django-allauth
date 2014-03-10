===============================
Running the example application
===============================

Assuming you use virtualenv, follow these steps to download and run the
demo-django-allauth example application in this directory:

::

    $ git clone git://github.com/dedcode/demo-django-allauth.git
    $ cd demo-django-allauth
    $ virtualenv venv
    $ . venv/bin/activate
    $ pip install -r requirements.txt
    $ python manage.py syncdb
    $ python manage.py runserver

You should then be able to open your browser on http://127.0.0.1:8000 and
see a page with links to sign in, sign up, manage accounts.

:: 
	You have to register you apps on Facebook, Twitter, LinkedIn to get keys and secrects
	then add these to the admin interface: http://127.0.0.1:8000/admin