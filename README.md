django-redis-shell
==================

Command line support for ./manage.py redisshell

## Installation:

1. Install via pip:

    $ pip install git+git://github.com/loisaidasam/django-redis-shell.git


2. Add "djangoredisshell" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'djangoredisshell',
    )


## Usage:

Shell access:

    ./manage.py redisshell

Read from shell:

    ./manage.py redisshell keys '*'

Delete from shell:

    ./manage.py redisshell keys '*' | xargs ./manage.py redisshell del
