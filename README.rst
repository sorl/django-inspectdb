
django-inspectdb
================

A fork of Django management command ``inspectdb``. It was first created to get
the correct ``max_length`` of MySQL inspection, see `ticket #5725`_.


Installation
------------
First install the package using pip::

    pip install django-inspectdb

Add it to your ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        ...
        'inspectdb',
        ...
    )


Usage
-----
Just use it as the normal `inspectdb management command`_::

    python manage.py inspectdb > models.py


.. _ticket #5725: http://code.djangoproject.com/ticket/5725
.. _inspectdb management command: http://docs.djangoproject.com/en/1.3/howto/legacy-databases/#auto-generate-the-models


