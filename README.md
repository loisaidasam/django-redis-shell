django-redis-shell
==================

Command line support for `./manage.py redisshell` (or `./manage.py rshell` for short)

## Installation:

Install via pip:

    $ pip install git+git://github.com/loisaidasam/django-redis-shell.git


Add "djangoredisshell" to your `INSTALLED_APPS` setting (in settings.py) like this::

    INSTALLED_APPS = (
        ...
        'djangoredisshell',
    )

Add a variable in settings.py called `REDIS_URL`

    REDIS_URL = 'redis://[username]:[password]@[host]:[port]'


## Usage:

Shell access:

    ./manage.py redisshell

Read from shell:

    ./manage.py redisshell keys '*'

Delete from shell:

    ./manage.py redisshell keys '*' | xargs ./manage.py redisshell del


## Notes:

The meat of this project is in this file:

[https://github.com/loisaidasam/django-redis-shell/blob/master/djangoredisshell/management/commands/redisshell.py](https://github.com/loisaidasam/django-redis-shell/blob/master/djangoredisshell/management/commands/redisshell.py)
