django-pudb
===========

Installing
----------

1. In your settings.py:
   - Add 'django_pudb.PudbMiddleware' at/near the end of your MIDDLEWARE_CLASSES
   - Set DEBUG_PROPAGATE_EXCEPTIONS = True
2. Run ./manage.py runserver --nothreading

Now you should see PUDB pop up in your console window whenever a view 
raises an exception.

Notes
-----

As PUDB doesn't support threading (yet, hopefully), django-pudb doesn't either.
