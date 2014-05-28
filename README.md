django-redis-shell
==================

## Installation:

    $ pip install git+git://github.com/loisaidasam/django-redis-shell.git


## Usage:

Shell access:

    ./manage.py redisshell

Read from shell:

    ./manage.py redisshell keys '*'

Delete from shell:

    ./manage.py redisshell keys '*' | xargs ./manage.py redisshell del
